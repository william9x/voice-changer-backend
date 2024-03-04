import logging
from io import BytesIO
from pathlib import Path

from fastapi import FastAPI
from fastapi import responses
from pydantic import BaseModel
from rvc.modules.vc.modules import VC
from scipy.io import wavfile
from starlette.responses import StreamingResponse

logger = logging.getLogger(__name__)

app = FastAPI()


class RvcInferReq(BaseModel):
    model_path: str
    index_file: Path | None = None
    input: Path
    sid: int = 0
    transpose: int = 0
    f0_method: str = "rmvpe"
    index_rate: float = 0.75
    filter_radius: int = 3
    resample_sr: int = 0
    rms_mix_rate: float = 0.25
    protect: float = 0.33


@app.post("/api/v1/rvc/infer", tags=["Infer"], response_class=StreamingResponse)
async def rvc_infer(req: RvcInferReq) -> StreamingResponse:
    vc = VC()
    vc.get_vc(req.model_path)
    tgt_sr, audio_opt, times, _ = vc.vc_single(
        sid=req.sid,
        input_audio_path=req.input,
        f0_up_key=req.transpose,
        f0_method=req.f0_method,
        f0_file=None,
        index_file=req.index_file,
        index_rate=req.index_rate,
        filter_radius=req.filter_radius,
        resample_sr=req.resample_sr,
        rms_mix_rate=req.rms_mix_rate,
        protect=req.protect,
    )
    wavfile.write(wv := BytesIO(), tgt_sr, audio_opt)
    print(times)
    return responses.StreamingResponse(
        wv,
        media_type="audio/wav",
        headers={"Content-Disposition": "attachment; filename=inference.wav"},
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)

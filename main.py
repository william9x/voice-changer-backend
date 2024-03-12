import logging
from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel
from scipy.io import wavfile
from starlette.responses import JSONResponse

from voice_model_factory import VoiceModelFactory

logger = logging.getLogger(__name__)

factory = VoiceModelFactory()

app = FastAPI()


class RvcInferReq(BaseModel):
    model_path: str
    index_path: Path | None = None
    input_path: Path
    output_path: Path
    sid: int = 0
    transpose: int = 0
    f0_method: str = "rmvpe"
    index_rate: float = 0.75
    filter_radius: int = 3
    resample_sr: int = 0
    rms_mix_rate: float = 0.25
    protect: float = 0.33


@app.post("/api/v1/rvc/infer", tags=["Infer"], response_class=JSONResponse)
async def rvc_infer(req: RvcInferReq) -> JSONResponse:
    print(f"received request: {req}")
    vc = factory.get_model(req.model_path)
    if vc is None:
        return JSONResponse(content={"message": f"Model {req.model_path} not exist"}, status_code=400)

    tgt_sr, audio_opt, times, _ = vc.vc_single(
        sid=req.sid,
        input_audio_path=req.input_path,
        f0_up_key=req.transpose,
        f0_method=req.f0_method,
        f0_file=None,
        index_file=req.index_path,
        index_rate=req.index_rate,
        filter_radius=req.filter_radius,
        resample_sr=req.resample_sr,
        rms_mix_rate=req.rms_mix_rate,
        protect=req.protect,
    )
    wavfile.write(req.output_path, tgt_sr, audio_opt)
    return JSONResponse(content={"message": "Created"}, status_code=201)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080, loop="asyncio", workers=15)

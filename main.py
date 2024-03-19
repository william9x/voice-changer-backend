import logging
from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel
from rvc.modules.vc.modules import VC
from scipy.io import wavfile
from starlette.responses import JSONResponse

logger = logging.getLogger(__name__)
app = FastAPI()


class RvcInferReq(BaseModel):
    model_path: str
    index_path: str
    input_path: str
    output_path: str
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
    vc = VC()
    vc.get_vc(req.model_path)
    if vc is None:
        return JSONResponse(content={"message": f"Model {req.model_path} not exist"}, status_code=400)

    _input_path = Path(req.input_path)
    print(f"input {_input_path.absolute()}")

    tgt_sr, audio_opt, times, _ = vc.vc_single(
        sid=req.sid,
        input_audio_path=Path(req.input_path),
        f0_up_key=req.transpose,
        f0_method=req.f0_method,
        f0_file=None,
        index_file=Path(req.index_path),
        index_rate=req.index_rate,
        filter_radius=req.filter_radius,
        resample_sr=req.resample_sr,
        rms_mix_rate=req.rms_mix_rate,
        protect=req.protect,
    )
    wavfile.write(req.output_path, tgt_sr, audio_opt)
    return JSONResponse(content={"message": "Created"}, status_code=201)

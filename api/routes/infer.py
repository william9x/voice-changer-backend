import logging

from fastapi import APIRouter
from pydantic import BaseModel
from starlette.responses import JSONResponse

from services import voice_changer

log = logging.getLogger(__name__)

router = APIRouter(prefix="/infer", tags=["Infer"])


class InferReq(BaseModel):
    input_path: str
    output_path: str
    model_path: str
    config_path: str
    transpose: int | None = 0


@router.post('/', response_class=JSONResponse)
async def infer(req: InferReq) -> JSONResponse:
    try:
        log.info(f"Infer request: {req}")
        voice_changer.infer(req.input_path, req.output_path, req.model_path, req.config_path, req.transpose)
    except Exception as e:
        log.error(e)
        return JSONResponse(status_code=500, content={"message": "Internal Server Error"})
    return JSONResponse(status_code=201, content={"message": "Created"})

import logging
from typing import Annotated

from fastapi import APIRouter, Form, File
from fastapi.responses import FileResponse
from pydantic import BaseModel

from internal.services.voice_changer import infer as _infer

log = logging.getLogger(__name__)

router = APIRouter(prefix="/infer", tags=["Infer"])


class ChatCompletionResponse(BaseModel):
    id: str
    model: str
    input_path: str
    output_path: str
    transpose: int


@router.post('/', response_class=FileResponse)
async def infer(
        file: Annotated[bytes, File()],
        model: Annotated[str, Form()],
        transpose: Annotated[int, Form()],
):
    resp = _infer(model, transpose, file)
    return FileResponse(resp.output_path, media_type='application/octet-stream', filename=resp.output_path.name)

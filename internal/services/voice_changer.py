import logging
import uuid
from os.path import dirname, abspath
from pathlib import Path

from pydantic import BaseModel
from so_vits_svc_fork.inference.main import infer as _infer

log = logging.getLogger(__name__)

_dirname = dirname(dirname(abspath(__file__)))
_result_dir = f"{_dirname}/resources/results"
_upload_dir = f"{_dirname}/resources/uploads"
_model_dir = f"{_dirname}/resources/logs/44k"

_models = {
    'biden': {'model_file': "G_20000.pth"},
    'trump': {'model_file': "G_68800.pth"},
    'obama': {'model_file': "G_50000.pth"},
    'nguyen_ngoc_ngan': {'model_file': "G_1001.pth"}
}


class InferenceResult(BaseModel):
    id: str
    input_path: Path
    output_path: Path


def infer(model: str, transpose: int, file: bytes) -> InferenceResult:
    _id = str(uuid.uuid4())
    input_path = Path(f"{_upload_dir}/{_id}.in.wav")
    output_path = Path(f"{_result_dir}/{_id}.out.wav")

    model_data = _models.get(model, None)
    if model_data is None:
        raise Exception(f"Model ${model} not found")

    model_file = Path(f"{_model_dir}/{model}/{model_data.get('model_file')}")
    config_file = Path(f"{_model_dir}/{model}/config.json")

    with open(input_path, mode='bx') as f:
        f.write(file)

    _infer(
        input_path=input_path,
        output_path=output_path,
        model_path=model_file,
        config_path=config_file,
        speaker=0,
        transpose=transpose
    )
    return InferenceResult(
        id=_id,
        input_path=input_path,
        output_path=output_path
    )

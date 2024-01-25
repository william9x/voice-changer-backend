import logging
from os.path import dirname, abspath

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


def infer(
        input_path: str,
        output_path: str,
        model_path: str,
        config_path: str,
        transpose: int,
):
    _infer(
        input_path=input_path,
        output_path=output_path,
        model_path=model_path,
        config_path=config_path,
        speaker=0,
        transpose=transpose
    )

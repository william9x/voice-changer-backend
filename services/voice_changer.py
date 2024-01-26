import logging

from so_vits_svc_fork.inference.main import infer as _infer

log = logging.getLogger(__name__)


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

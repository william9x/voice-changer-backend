import os
from pathlib import Path

import requests

RVC_DOWNLOAD_LINK = "https://huggingface.co/liamhvn/voice-models/resolve/main/rvc/"

BASE_DIR = Path(__file__).resolve().parent.parent


def dl_model(link, model_name, dir_name):
    with requests.get(f"{link}{model_name}") as r:
        r.raise_for_status()
        os.makedirs(os.path.dirname(dir_name / model_name), exist_ok=True)
        with open(dir_name / model_name, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)


if __name__ == "__main__":
    model_paths = [
        "elon_musk/",
        "trump/",
        "taylor_swift/",
    ]
    for model in model_paths:
        print(f"Downloading {model}...")
        rvc_models_dir = BASE_DIR / "assets/weights/rvc" / model
        dl_model(RVC_DOWNLOAD_LINK + model, "G.pth", rvc_models_dir)
        dl_model(RVC_DOWNLOAD_LINK + model, "model.index", rvc_models_dir)

    print("All models downloaded!")

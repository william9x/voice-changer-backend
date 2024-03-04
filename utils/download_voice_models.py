from pathlib import Path

from utils.download_models import dl_model

RVC_DOWNLOAD_LINK = "https://huggingface.co/liamhvn/voice-models/resolve/main/rvc/"

BASE_DIR = Path(__file__).resolve().parent.parent

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

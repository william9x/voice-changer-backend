import os
from pathlib import Path

import requests

RVC_DOWNLOAD_LINK = "https://huggingface.co/liamhvn/voice-models/resolve/main/rvc"

BASE_DIR = Path(__file__).resolve().parent.parent


def dl_model(link, dir_name, output_file):
    with requests.get(f"{link}") as r:
        r.raise_for_status()
        os.makedirs(os.path.dirname(dir_name / output_file), exist_ok=True)
        with open(dir_name / output_file, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)


if __name__ == "__main__":
    rvc_models_dir = BASE_DIR / "assets/weights/"
    model_paths = [
        "trump",
        "elon_musk",
        "taylor_swift",
        "obama",
        "jung_kook",
        "charlie_puth",
        "doja_cat",
        "justin_bieber",
        "biden",
        "wrld_juice",
        "patrick_star",
        "katy_perry",
        "jay_z",
        "dua_lipa",
        "bts_jimin",
        "homer_simpson",
        "the_weeknd",
        "lady_gaga",
        "nicki_minaj",
        "blackpink_jennie",
        "redvelvet_irene",
        "bad_bunny",
        "elton_john",
        "harry_styles",
        "troye_sivan",
        "britney_spears",
        "bruno_mars",
        "chris_brown",
        "blackpink_jiso",
        "rosalia",
        "bilie_eilish",
        "ariana_grande",
        "olivia_rodrigo",
        "rihanna",
        "starrail_seele",
        "snsd_taeyeon",
        "bts_jhope",
        "bts_suga",
        "starrail_7th",
        "bts_taehyung",
        "jack_black",
        "quasimoto",
        "post_malone",
        "21savage",
        "kim_jong_un",
        "putin",
        "mickey_mouse",
        "batman",
        "messi",
        "godzilla",
    ]
    for model in model_paths:
        print(f"Downloading {model}...")
        dl_model(f"{RVC_DOWNLOAD_LINK}/{model}.pth", rvc_models_dir, f"{model}.pth")
        dl_model(f"{RVC_DOWNLOAD_LINK}/{model}.index", rvc_models_dir, f"{model}.index")

    print("All models downloaded!")

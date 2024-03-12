from rvc.modules.vc.modules import VC

MODEL_IDS = [
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


class VoiceModelFactory:
    def __init__(self):
        self._models = {}

        for model in MODEL_IDS:
            self.init_models(model)

    def init_models(self, model_id):
        print(f"Loading model ${model_id}")
        vc = VC()
        self._models[model_id] = vc.get_vc(model_id)

    def get_model(self, model_id):
        print(f"Model selected: {model_id}")
        return self._models.get(model_id)

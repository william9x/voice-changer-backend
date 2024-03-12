from rvc.modules.vc.modules import VC

MODEL_PATHS = [
    "trump.pth",
    "elon_musk.pth",
    "taylor_swift.pth",
    "obama.pth",
    "jung_kook.pth",
    "charlie_puth.pth",
    "doja_cat.pth",
    "justin_bieber.pth",
    "biden.pth",
    "wrld_juice.pth",
    "patrick_star.pth",
    "katy_perry.pth",
    "jay_z.pth",
    "dua_lipa.pth",
    "bts_jimin.pth",
    "homer_simpson.pth",
    "the_weeknd.pth",
    "lady_gaga.pth",
    "nicki_minaj.pth",
    "blackpink_jennie.pth",
    "redvelvet_irene.pth",
    "bad_bunny.pth",
    "elton_john.pth",
    "harry_styles.pth",
    "troye_sivan.pth",
    "britney_spears.pth",
    "bruno_mars.pth",
    "chris_brown.pth",
    "blackpink_jiso.pth",
    "rosalia.pth",
    "bilie_eilish.pth",
    "ariana_grande.pth",
    "olivia_rodrigo.pth",
    "rihanna.pth",
    "starrail_seele.pth",
    "snsd_taeyeon.pth",
    "bts_jhope.pth",
    "bts_suga.pth",
    "starrail_7th.pth",
    "bts_taehyung.pth",
    "jack_black.pth",
    "quasimoto.pth",
    "post_malone.pth",
    "21savage.pth",
    "kim_jong_un.pth",
    "putin.pth",
    "mickey_mouse.pth",
    "batman.pth",
    "messi.pth",
    "godzilla.pth",
]


class VoiceModelFactory:
    def __init__(self):
        self._models = {}

        for path in MODEL_PATHS:
            self.init_models(path)

    def init_models(self, model_path):
        print(f"Loading model ${model_path}")
        vc = VC()
        self._models[model_path] = vc.get_vc(model_path)

    def get_model(self, model_path):
        print(f"Model selected: {model_path}")
        return self._models.get(model_path)

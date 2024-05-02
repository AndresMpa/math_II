import os
from pathlib import Path
from dotenv import load_dotenv
from os.path import join, dirname


project_path = Path(dirname(__file__))
env_file = join(project_path.parent.absolute(), ".env")

load_dotenv(env_file)

config = {
    "mode": os.environ.get("MODE"),

    "image_size": int(os.environ.get("IMAGE_SIZE", 200)),
    "image_dir": os.environ.get("IMAGE_DIR"),

    "mtx_dir": os.environ.get("MATRIX_DIR"),
    "mtx_max": int(os.environ.get("MATRIX_MAX", 200)),
    "mtx_min": int(os.environ.get("MATRIX_MIN", 0)),

    "save_image_dir": os.environ.get("SAVE_IMAGE_DIR"),
    "save_matrix_dir": os.environ.get("SAVE_MATRIX_DIR"),

    "web_site": os.environ.get("WEB_SITE"),

    "verbose": os.environ.get("VERBOSE") == "1",
    "autoclear": os.environ.get("AUTOCLEAR") == "1",
}

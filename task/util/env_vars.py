import os
from pathlib import Path
from dotenv import load_dotenv
from os.path import join, dirname


project_path = Path(dirname(__file__))
env_file = join(project_path.parent.absolute(), ".env")

load_dotenv(env_file)

config = {
    "mode": os.environ.get("MODE"),

    "image_dir": os.environ.get("IMAGE_DIR"),
    "save_dir": os.environ.get("SAVE_DIR"),

    "web_site": os.environ.get("WEB_SITE"),

    "verbose": os.environ.get("VERBOSE") == "1",
    "autoclear": os.environ.get("AUTOCLEAR") == "1",
}

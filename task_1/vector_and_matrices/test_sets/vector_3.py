from util.image import create_random, load_image, save_image
from vectors.main import tighten
from util.env_vars import config


def vector_3(timestamp: str) -> None:
    factor = config["image_tighten_factor"]
    create_random(
        [config["image_size"]],
        f"TV3_tf-{str(factor)}_{timestamp}")
    image = load_image()

    moded_image = tighten(image, factor)
    save_image(
        moded_image,
        f"TV3_tf-{str(factor)}_{timestamp}")

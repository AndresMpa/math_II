from util.image import create_random, load_image, save_image
from vectors.main import tighten
from util.env_vars import config


def vector_3(timestamp: str) -> None:
    create_random([config["image_size"]], "test")
    image = load_image()

    factor = 2
    moded_image = tighten(image, factor)
    save_image(
        moded_image,
        f"TV3_tf-{str(factor)}_{timestamp}")

from util.image import create_random, load_image, save_image
from vectors.main import stretch
from util.env_vars import config


def vector_2(timestamp: str) -> None:
    factor = config["image_stretch_factor"]
    create_random(
        [config["image_size"]],
        f"TV2_sf-{str(factor)}_{timestamp}")
    image = load_image()

    moded_image = stretch(image, factor)
    save_image(
        moded_image,
        f"TV2_sf-{str(factor)}_{timestamp}")

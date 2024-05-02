from util.image import create_random, load_image, save_image
from vectors.main import stretch
from util.env_vars import config


def vector_2(timestamp: str) -> None:
    create_random([config["image_size"]], "test")
    image = load_image()

    factor = 2
    moded_image = stretch(image, factor)
    save_image(
        moded_image,
        f"TV2_sf-{str(factor)}_{timestamp}")

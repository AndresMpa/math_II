from random import uniform

from util.image import create_random, load_image, save_image
from vectors.main import degrees_to_radians, rotate
from util.env_vars import config


def vector_1(timestamp: str) -> None:
    create_random([config["image_size"]], "test")
    image = load_image()
    degrees = uniform(0, 360)

    angle = degrees_to_radians(degrees)
    moded_image = rotate(image, angle)
    save_image(
        moded_image,
        f"TV1_d-{str(degrees)}_s-{str(config['image_size'])}_{timestamp}")

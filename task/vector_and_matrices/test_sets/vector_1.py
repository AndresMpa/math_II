from random import uniform

from util.image import create_random, load_image, save_image
from vectors.main import degrees_to_radians, rotate
from util.env_vars import config


def vector_1(timestamp: str) -> None:
    degrees = uniform(0, 360)
    create_random(
        [config["image_size"]],
        f"TV1_d-{str(degrees)}_s-{str(config['image_size'])}_{timestamp}")
    image = load_image()

    angle = degrees_to_radians(degrees)
    moded_image = rotate(image, angle)
    save_image(
        moded_image,
        f"TV1_d-{str(degrees)}_s-{str(config['image_size'])}_{timestamp}")

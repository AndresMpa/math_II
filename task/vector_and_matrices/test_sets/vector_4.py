from random import uniform

from util.image import create_random, load_image, save_image
from vectors.main import degrees_to_radians, rotate, tighten, stretch
from util.env_vars import config


def vector_4(timestamp: str) -> None:
    create_random([config["image_size"]], "test")
    image = load_image()
    degrees = uniform(0, 360)

    factor = [4, 10]
    angle = degrees_to_radians(degrees)

    moded_image = rotate(image, angle)
    moded_image = stretch(moded_image, factor[0])
    moded_image = tighten(moded_image, factor[1])

    save_image(
        moded_image,
        f"TV4_d-{str(degrees)}_s-{str(config['image_size'])}_tf-{str(factor)}_sf-{str(factor)}_{timestamp}")

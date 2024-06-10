from random import uniform

from util.image import create_random, load_image, save_image
from vectors.main import degrees_to_radians, rotate, tighten, stretch
from util.env_vars import config


def vector_4(timestamp: str) -> None:
    degrees = uniform(0, 360)
    angle = degrees_to_radians(degrees)

    tighten_factor = config["image_tighten_factor"]
    stretch_factor = config["image_stretch_factor"]

    create_random([config["image_size"]],
                  f"TV4_s-{
        str(config['image_size'])
    }_d-{
        str(degrees)
    }_tf-{
        str(tighten_factor)
    }_sf-{
        str(stretch_factor)
    }_{timestamp}")

    image = load_image()

    moded_image = rotate(image, angle)
    moded_image = stretch(moded_image, stretch_factor)
    moded_image = tighten(moded_image, tighten_factor)

    save_image(
        moded_image,
        f"TV4_s-{
            str(config['image_size'])
        }_d-{
            str(degrees)
        }_tf-{
            str(tighten_factor)
        }_sf-{
            str(stretch_factor)
        }_{timestamp}")

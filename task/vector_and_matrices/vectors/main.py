from PIL import Image
from typing import Tuple
from math import cos, sin, pi
from numpy import array, zeros, uint8


def degrees_to_radians(
    degrees: float
) -> float:
    """
    Convert degrees to radians

    Agrs:
        degrees (int): A number (0 to 360), that means a angle

    Returns:
        Returns the equivalent in radians
    """
    return degrees * (pi / 180.0)


def stretch(
    image: Image.Image,
    stretch_factor: int
) -> Image.Image:
    """
    Stretch an image given a factor casting its byte rate to arrays

    Args:
        image (Image.Image): An image from pillow
        stretch_factor (int): A factor as a integer

    Returns:
        An image casted from an array
    """
    image_array = array(image)
    height, width, dim = image_array.shape

    featured_width = int(width * stretch_factor)
    longed_image = zeros((height, featured_width, dim), dtype=uint8)

    print("shape ", image_array.shape)
    print("shape ", longed_image.shape)

    for y in range(height):
        for x in range(featured_width):
            original_x = int(x / stretch_factor)
            longed_image[y, x] = image_array[y, original_x]

    return Image.fromarray(longed_image)


def tighten(
    image: Image.Image,
    tighten_factor: int
) -> Image.Image:
    """
    Tighten an image given a factor casting its byte rate to arrays

    Args:
        image (Image.Image): An image from pillow
        tighten_factor (int): A factor as a integer

    Returns:
        An image casted from an array
    """
    image_array = array(image)
    height, width, dim = image_array.shape

    featured_height = int(height * tighten_factor)
    image_achatada = zeros((featured_height, width, dim), dtype=uint8)

    for y in range(featured_height):
        for x in range(width):
            original_y = int(y / tighten_factor)
            image_achatada[y, x] = image_array[original_y, x]

    return Image.fromarray(image_achatada)


def rotate_point(
    point: Tuple[float, float],
    angle: float
) -> Tuple[float, float]:
    """
    It rotates a point

    Args:
        point (Tuple[float, float]): A simple par of points
        angle (float): A factor as an angle

    Returns:
        A simple par of points casted
    """
    x, y = point
    x_rotated = x * cos(angle) - y * sin(angle)
    y_rotated = x * sin(angle) + y * cos(angle)
    return x_rotated, y_rotated


def rotate(
    image: Image.Image,
    angle: float
) -> Image.Image:
    """
    It rotates an image given an angle

    Args:
        image (Image.Image): An image object from pillow
        angle (float): A simple factor as an angle

    Returns:
        It rotates an image
    """
    width, height = image.size
    image = image.convert("RGBA")

    rotated_image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    center_x, center_y = width / 2, height / 2
    pixels = array(image)

    for x in range(width):
        for y in range(height):
            rel_x, rel_y = x - center_x, y - center_y
            rotated_x, rotated_y = rotate_point((rel_x, rel_y), angle)
            rotated_x, rotated_y = rotated_x + center_x, rotated_y + center_y

            if 0 <= rotated_x < width and 0 <= rotated_y < height:
                rotated_image.putpixel(
                    (x, y),
                    tuple(pixels[int(rotated_x), int(rotated_y)])
                )

    return rotated_image

import os
import requests

from PIL import Image
from typing import List
from random import randint

from util.env_vars import config
from util.dirs import create_dir, clear_dir
from util.dirs import check_path, create_path, get_current_path


def create_random(size: List[int], file_name: str, file_extention: str = "jpg") -> None:
    """
    Create a file from config given a size and its file name

    Args:
        size (list[int]): List of integers
        file_name (str): File name
        file_extention (str): File extention
    """
    if (len(size) == 1):
        image = f'{config["web_site"]}/{size}'
    else:
        image = f'{config["web_site"]}/{size[0]}/{size[1]}'

    response = requests.get(image)

    if not check_path(config["image_dir"]):
        create_dir(config["image_dir"])

    file_path = create_path(
        config["image_dir"], f"{file_name}.{file_extention}")

    if response.status_code == 200:
        with open(f"{file_path}", "wb") as f:
            f.write(response.content)
        print(f"Image donwloaded at {file_path}")
    else:
        print(f"[ERROR] donwloading image {response.status_code}")


def load_image(file_name: str = "") -> Image.Image:
    """
    Loads file_name or a random file from config

    Args:
        file_extention (str): Specific image to load

    Note:
        Default is random

    Returns:
        Image from pillow
    """
    try:
        path = get_current_path(config['image_dir'])
        files = os.listdir(path)
        if file_name != "":
            idx = randint(0, len(files) - 1)
        else:
            idx = files.index(file_name)

        if not check_path(f"{config['image_dir']}/{files[idx]}"):
            print(
                f"[ERROR]: File was not found {config['image_dir']}/{files[idx]}")

        file_path = os.path.join(path, files[idx])

        if os.path.isfile(file_path):
            image = Image.open(f"{file_path}")
            return image
    except OSError:
        print(
            f"[ERROR]: Something went wrong while getting image {file_name} or index not found")


def save_image(image: Image.Image, file_name: str, file_extention: str = "jpg") -> None:
    """
    Saves a pillow kind image

    Args:
        image (Image): A pillow image
        file_name (str): A specific file name
        file_extention (str): The specific image file extention (Default is jpg)
    """
    try:
        if not check_path(f"{config['save_dir']}/{file_name}"):
            create_dir(config["save_dir"])
        image.save(f"{config['save_dir']}/{file_name}.{file_extention}")
    except OSError:
        print(
            f"[ERROR]: Something went wrong while saving the file {file_name}")


def clear_images():
    """
    Removes all data from respective directories
    """
    if (config["autoclear"]):
        for dir in ["save_dir"]:
            path = get_current_path(config[dir])
            clear_dir(path)

import time
from util.env_vars import config
from util.image import clear_images
from test_sets.main import select_stage

if __name__ == '__main__':
    timestamp = str(time.time())

    test = select_stage(config["mode"])

    if test == "Error":
        raise Exception("There is an error on your .env file")

    test(timestamp)
    clear_images()

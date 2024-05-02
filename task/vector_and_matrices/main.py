import time
from util.env_vars import config
from test_sets.main import select_stage
from util.dirs import clear_dir, get_current_path

if __name__ == '__main__':
    if (config["autoclear"]):
        clear_dir(get_current_path(config['mtx_dir']))
        clear_dir(get_current_path(config['image_dir']))
        clear_dir(get_current_path(config['save_image_dir']))
        clear_dir(get_current_path(config['save_matrix_dir']))

    timestamp = str(time.time())

    test = select_stage(config["mode"])

    if test == "Error":
        raise Exception("There is an error on your .env file")

    test(timestamp)

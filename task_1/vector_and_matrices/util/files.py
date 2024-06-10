import os
import csv
from typing import List
from warnings import warn
from numpy import ndarray, array

from util.dirs import check_path, create_path, get_current_path
from util.dirs import create_dir
from util.env_vars import config


def save_as_csv(data: ndarray, file_name: str) -> None:
    """
    Create a CSV file using a numpy array as data

    Args:
        data (ndarray): A simple numpy array
        file_name (str): Given file name
    """
    if not check_path(config["save_matrix_dir"]):
        create_dir(config["save_matrix_dir"])

    file_path = create_path(config["save_matrix_dir"], f"{file_name}.csv")

    with open(f"{file_path}", mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"')
        for row in data:
            writer.writerow(row)


def load_csv_file() -> List[ndarray]:
    """
    It loads all csv type files from mtx_dir then creates a list of ndarrays

    Returns:
        List of data in ram as ndarray
    """
    csv_data = []
    if not check_path(config["mtx_dir"]):
        warn(
            f"[WARNING]: Directory {config['mtx_dir']} not found. Creating it",
            RuntimeWarning,
            stacklevel=2
        )
        create_dir(config["mtx_dir"])

    path = get_current_path(config['mtx_dir'])
    files = os.listdir(path)

    if (len(files) == 0):
        warn(
            f"[WARNING]: No files provided at {config['mtx_dir']}",
            RuntimeWarning,
            stacklevel=1)

        return csv_data

    for file_name in files:
        file_path = create_path(config["mtx_dir"], file_name)

        with open(f'{file_path}', 'r') as file:
            lines = file.readlines()
            raw_data = []

            for line in lines:
                columns = line.strip().split(',')
                raw_data.append([float(x) for x in columns])

        csv_data.append(array(raw_data))

    return csv_data

import csv
from numpy import ndarray

from util.dirs import check_path, create_path, create_dir
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
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)

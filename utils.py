import os


def load_input(file_name):
    with open(os.path.join("inputs", file_name), "r") as f:
        ret = f.read()[:-1]
    return ret

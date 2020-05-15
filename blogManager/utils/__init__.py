import os


def get_current_path(file=__file__):
    return os.path.dirname(os.path.abspath(file))


def to_path(*path):
    return os.path.join(*path)


def make_dir(path, mode=0o777, exist_ok=True):
    os.makedirs(path, mode, exist_ok=exist_ok)


if __name__ == '__main__':
    print(to_path('1,3,4,5', '123123', '123dfgdsfgdsfgds'))

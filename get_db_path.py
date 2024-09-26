import sys


def get_db_path():
    # Проверяем, передан ли хотя бы один аргумент
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        raise ValueError("U need to pass db path to argument")
        return None

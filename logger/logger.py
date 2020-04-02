import os
import datetime
from pathlib import Path


def parameterized(path: str):
    separate_path = path.split('/')
    file_name = separate_path.pop()
    folder_path = '/'.join(separate_path)
    os.makedirs(Path(folder_path))

    def logger_decor(old_function):
        def log_func(*args, **kwargs):
            with open(Path(folder_path) / file_name, 'w', encoding='utf-8') as log_file:
                log_file.write(f'{datetime.datetime.now()} \n')
                log_file.write(f'function name: {old_function.__name__} \n')
                log_file.write(f'function args: { {"args": args, "kwargs": kwargs } } \n')
                log_file.write(f'returned value: {old_function()} \n')
        return log_func
    return logger_decor


if __name__ == '__main__':
    @parameterized('logs/test/logger.txt')
    def test_func(*args, **kwargs):
        return 2 + 2


    test_func(1, 2, 55, test='123')

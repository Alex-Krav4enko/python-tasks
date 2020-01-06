import datetime


class CustomCM:
    def __init__(self, path, encoding='utf8'):
        self.path = path
        self.encoding = encoding

    def __enter__(self):
        self.file = open(self.path, encoding=self.encoding)
        self.start = datetime.datetime.now()
        print(f'{self.start=}')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        self.end = datetime.datetime.now()
        print(f'{self.end=}')
        print(f'spend time: {self.end - self.start}')

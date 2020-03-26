import json


class Countries:
    def __init__(self, path):
        self.index = None
        self.path = path
        with open(self.path, encoding='utf-8') as file:
            self.countries = json.load(file)

    def __iter__(self):
        return self

    def __next__(self):
        self.index = 0 if (self.index is None) else (self.index + 1)
        if self.index > (len(self.countries) - 1):
            raise StopIteration
        name = self.get_country(self.index)['name']['common']
        return f'https://ru.wikipedia.org/wiki/{name}'

    def get_country(self, i):
        return self.countries[i]


if __name__ == '__main__':
    for url in Countries('countries.json'):
        print(url)


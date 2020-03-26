import hashlib


def countries(path):
    with open(path, encoding='utf-8') as file:
        for line in file:
            yield hashlib.md5(line.encode('utf-8'))


if __name__ == '__main__':
    for hash_line in countries('countries.json'):
        print(hash_line)
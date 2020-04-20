from pymongo import MongoClient
from pymongo import ASCENDING
from pprint import pprint
import csv
import re


def read_data(csv_file, collection):
    with open(csv_file, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        collection.insert_many(list(reader))


def find_cheapest(collection):
    return list(collection.find().sort('Цена', ASCENDING))


def find_by_name(collection, name):
    pattern = re.compile(name, re.IGNORECASE)
    return list(collection.find({'Исполнитель': pattern}).sort('Цена', ASCENDING))


if __name__ == '__main__':
    client = MongoClient()
    concerts_db = client['concerts_db']
    concerts = concerts_db['data']

    # read_data('artists.csv', concerts)
    # pprint(find_cheapest(concerts))
    # pprint(find_by_name(concerts, 'н с'))

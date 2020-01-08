import requests
import os


API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_it(path_source, path_res, from_lang, to_lang='ru'):

    with open(path_source) as source_file:
        source_data = source_file.read()
        file_name = source_file.name

    params = {
        'key': API_KEY,
        'text': source_data,
        'lang': f'{from_lang}-{to_lang}',
    }

    response = requests.get(URL, params=params)
    result_directory = os.path.join(os.getcwd(), path_res)
    result_address = os.path.join(result_directory, file_name)
    json_ = response.json()

    if not os.path.isdir(result_directory):
        os.mkdir(result_directory)

    with open(result_address, 'w') as res_file:
        res_file.write(''.join(json_['text']))


translate_it('DE.txt', 'result', 'de')
translate_it('ES.txt', 'result', 'es')
translate_it('FR.txt', 'result', 'fr')

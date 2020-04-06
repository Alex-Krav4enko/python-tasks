import requests


class Translator:
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    query_params = dict(
        key='trnsl.1.1.20200405T150959Z.59588fea42af6458.53b89b92c8c100fb159791b6ea7821ada02e6db1',
        lang='ru-en',
        text=None
    )

    def _get_params(self, translate_text):
        self.query_params['text'] = translate_text
        params_list = list(self.query_params.items())
        params_list = map(lambda x: '='.join(x), params_list)
        return '&'.join(list(params_list))

    def translate(self, translate_text):
        params = self._get_params(translate_text)
        return requests.get(self.url, params).json()


if __name__ == '__main__':
    translator = Translator()
    print(translator.translate('кот'))

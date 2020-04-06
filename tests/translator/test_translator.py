import unittest
from tests.translator import translator


class TestTranslator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.translator = translator.Translator()

    def test_create_params(self):
        params = self.translator._get_params('test')
        self.assertTrue(isinstance(params, str))

    def test_raise_exc_params(self):
        self.assertRaises(TypeError, self.translator._get_params, None)

    def test_response_status(self):
        res = self.translator.translate('test')
        self.assertEqual(res['code'], 200)

    def test_correct_translation(self):
        res = self.translator.translate('кот')
        self.assertEqual(''.join(res['text']), 'cat')

from unittest import TestCase
import tests.app as app


class TestBaseClass(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.dirs, cls.docs = app.update_date()
        cls.direct = app.Directories(cls.dirs, cls.docs)

    def test_document(self):
        doc_number = '10006'
        doc = self.direct.get_documents(doc_number)
        self.assertEqual(doc['number'], doc_number)

    def test_dir(self):
        shelf = self.direct.get_dir('1')
        self.assertIn('11-2', shelf)

import unittest
from zendesk import ZendeskSearch


class TestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_zendesk_input_validate(self):
        self.assertEqual(ZendeskSearch._input_validate(self, 1, 1, 2, "search_opt"), 1)

    def test_zendesk_input_validate_incorrect(self):
        self.assertEqual(ZendeskSearch._input_validate(self, 5, 1, 2), None)

    def test_check_quit(self):
        self.assertEqual(ZendeskSearch._check_quit(self, "invalid"), None)


if __name__ == '__main__':
    unittest.main(verbosity=2)

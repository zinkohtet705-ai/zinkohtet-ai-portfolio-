import unittest
from assistant.core import respond

class CoreTests(unittest.TestCase):
    def test_empty_message(self):
        self.assertEqual(respond(""), "Please enter a message.")

    def test_non_empty_message(self):
        self.assertIn("starter is running", respond("Hello"))

if __name__ == "__main__":
    unittest.main()

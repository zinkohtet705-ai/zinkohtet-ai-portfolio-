import unittest
from unittest.mock import patch

from assistant.core import respond

class CoreTests(unittest.TestCase):
    def test_empty_message(self):
        self.assertEqual(respond(""), "Please enter a message.")

    @patch("assistant.core.ask_model", return_value=None)
    def test_missing_api_key_uses_safe_message(self, mock_model):
        self.assertIn("OPENAI_API_KEY", respond("Hello"))

    @patch("assistant.core.ask_model", return_value="Hello from the model")
    def test_model_response(self, mock_model):
        self.assertEqual(respond("Hello"), "Hello from the model")

if __name__ == "__main__":
    unittest.main()

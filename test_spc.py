import unittest
from src.spc import spc_encode_message, spc_decode_message

class TestSPCFunctions(unittest.TestCase):
    def test_encode_basic(self):
        plaintext = "HELLO"
        key_numbers = [33]
        formatting = {"commas": False, "periods": False}
        encoded = spc_encode_message(plaintext, key_numbers, formatting)
        self.assertEqual(encoded, "8 5 33 12 12 15")

    def test_decode_basic(self):
        encoded_message = "8 5 33 12 12 15"
        decoded = spc_decode_message(encoded_message)
        self.assertEqual(decoded, "HELLO")

    def test_encode_with_formatting(self):
        plaintext = "WORLD"
        key_numbers = [13]
        formatting = {"commas": True, "periods": True}
        encoded = spc_encode_message(plaintext, key_numbers, formatting)
        self.assertTrue("," in encoded and "." in encoded)

    def test_decode_with_formatting(self):
        encoded_message = "23,15,18,13,4."
        decoded = spc_decode_message(encoded_message)
        self.assertEqual(decoded, "WORLD")

if __name__ == "__main__":
    unittest.main()
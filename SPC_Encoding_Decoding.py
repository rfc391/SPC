# SPC Encoding/Decoding Implementation Without Protobuf
from datetime import datetime
import unittest

# SPC Encoding Function (Example based on the guide)
def spc_encode_message(message, key_numbers, formatting):
    """
    Encodes a message using Symbolic Pattern Cryptography.
    :param message: Plaintext message to encode.
    :param key_numbers: List of key numbers to embed in encoding.
    :param formatting: Formatting rules (spaces, commas, etc.).
    :return: SPC-encoded string.
    """
    encoded_message = []
    for char in message:
        if char.isalpha():
            # Convert to numerical value A=1, B=2, ..., Z=26
            value = ord(char.upper()) - 64
            encoded_message.append(str(value))
        else:
            encoded_message.append(char)  # Non-alphabetic characters stay as is

    # Add key numbers at logical breaks (e.g., every 3 characters)
    for key in key_numbers:
        encoded_message.insert(len(encoded_message) // 2, str(key))

    # Apply formatting (e.g., commas, spaces)
    if formatting.get("commas"):
        encoded_message = [",".join(encoded_message)]
    if formatting.get("periods"):
        encoded_message.append(".")

    return " ".join(encoded_message)

# SPC Decoding Function
def spc_decode_message(encoded_message):
    """
    Decodes an SPC-encoded message.
    :param encoded_message: Encoded message.
    :return: Decoded plaintext message.
    """
    elements = encoded_message.replace(",", " ").replace(".", "").split()
    decoded_message = []

    for elem in elements:
        if elem.isdigit():
            # Convert numerical value back to letter
            value = int(elem)
            if 1 <= value <= 26:
                decoded_message.append(chr(value + 64))
        else:
            decoded_message.append(elem)  # Non-numeric characters stay as is

    return "".join(decoded_message)

# Example Workflow
def spc_workflow():
    plaintext = "MEET AT 3 PM"
    key_numbers = [33]  # Example key number
    formatting = {"commas": True, "periods": True}  # Example formatting rules

    # Step 1: Encode with SPC
    spc_encoded = spc_encode_message(plaintext, key_numbers, formatting)

    # Step 2: Decode the SPC message
    decoded_message = spc_decode_message(spc_encoded)

    # Display Results
    print("Original Message:", plaintext)
    print("SPC Encoded Payload:", spc_encoded)
    print("Decoded SPC Message:", decoded_message)

# Unit Tests
class TestSPCFunctions(unittest.TestCase):
    def test_encode_basic(self):
        plaintext = "HELLO"
        key_numbers = [33]
        formatting = {"commas": False, "periods": False}
        encoded = spc_encode_message(plaintext, key_numbers, formatting)
        expected = "8 5 33 12 12 15"
        self.assertEqual(encoded, expected)

    def test_decode_basic(self):
        encoded_message = "8 5 33 12 12 15"
        decoded = spc_decode_message(encoded_message)
        expected = "HELLO"
        self.assertEqual(decoded, expected)

    def test_encode_with_formatting(self):
        plaintext = "WORLD"
        key_numbers = [13]
        formatting = {"commas": True, "periods": True}
        encoded = spc_encode_message(plaintext, key_numbers, formatting)
        self.assertTrue("," in encoded and "." in encoded)

    def test_decode_with_formatting(self):
        encoded_message = "23,15,18,13,4."
        decoded = spc_decode_message(encoded_message)
        expected = "WORLD"
        self.assertEqual(decoded, expected)

if __name__ == "__main__":
    spc_workflow()
    unittest.main()

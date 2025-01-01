# Symbolic Pattern Cryptography (SPC) Project

## Overview
Symbolic Pattern Cryptography (SPC) is a novel approach to cryptography that uses numerical encoding and symbolic formatting to secure messages. This project implements SPC encoding and decoding in Python.

## Features
- Encode plaintext messages into SPC-encoded strings.
- Decode SPC-encoded strings back to plaintext.
- Customizable key numbers and formatting rules.
- Comprehensive unit tests for validation.

## Project Structure
```
SPC_Project/
├── src/
│   ├── spc.py       # Main implementation of SPC functions
├── tests/
│   ├── test_spc.py  # Unit tests for SPC encoding/decoding
├── README.md        # Project documentation
├── docs/
│   ├── guide.md     # SPC principles and usage
│   ├── usage_examples.md # Detailed examples
├── workflows/
│   ├── encoding_workflow.json
│   ├── decoding_workflow.json
```
## Usage
### Encoding a Message
```python
from src.spc import spc_encode_message

message = "HELLO"
key_numbers = [33]
formatting = {"commas": True, "periods": True}
encoded_message = spc_encode_message(message, key_numbers, formatting)
print(encoded_message)
```

### Decoding a Message
```python
from src.spc import spc_decode_message

encoded_message = "8,5,33,12,12,15."
decoded_message = spc_decode_message(encoded_message)
print(decoded_message)
```

## Running Tests
To run unit tests:
```bash
python -m unittest discover -s tests
```
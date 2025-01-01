# SPC Usage Examples

## Encoding Example
```python
from src.spc import spc_encode_message

plaintext = "SECRET"
key_numbers = [13, 42]
formatting = {"commas": True, "periods": True}
encoded = spc_encode_message(plaintext, key_numbers, formatting)
print(encoded)
```

## Decoding Example
```python
from src.spc import spc_decode_message

encoded = "19,5,3,13,18,20."
decoded = spc_decode_message(encoded)
print(decoded)
```
from datetime import datetime

def spc_encode_message(message, key_numbers, formatting):
    encoded_message = []
    for char in message:
        if char.isalpha():
            value = ord(char.upper()) - 64
            encoded_message.append(str(value))
        else:
            encoded_message.append(char)
    for key in key_numbers:
        encoded_message.insert(len(encoded_message) // 2, str(key))
    if formatting.get("commas"):
        encoded_message = [",".join(encoded_message)]
    if formatting.get("periods"):
        encoded_message.append(".")
    return " ".join(encoded_message)

def spc_decode_message(encoded_message):
    elements = encoded_message.replace(",", " ").replace(".", "").split()
    decoded_message = []
    for elem in elements:
        if elem.isdigit():
            value = int(elem)
            if 1 <= value <= 26:
                decoded_message.append(chr(value + 64))
        else:
            decoded_message.append(elem)
    return "".join(decoded_message)
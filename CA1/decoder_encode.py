# Task 3 & 4: Decode and Encode function

def decode(text):
    """Decodes a secret message by replacing encoded characters."""
    vowels = {"!": "a", "&": "e", "4": "i", "%": "o", ")": "u"}
    secret = ""
    for char in text:
        if char in vowels:
            secret += vowels[char]
        else:
            secret += char
    return secret


def encode(text):
    """Encodes a message using the dictionary."""
    vowels = {"!": "a", "&": "e", "4": "i", "%": "o", ")": "u"}
    vowels_encoded = {v: k for k, v in vowels.items()}

    secret = ""
    for char in text:
        if char in vowels_encoded:
            secret += vowels_encoded[char]
        else:
            secret += char
    return secret




def decode_encode(text, mode):
    """Decodes or encodes a message based on the mode."""
    if mode == "decode":
        return decode(text)
    elif mode == "encode":
        return encode(text)
    else:
        return ValueError("Mode must be 'decode' or 'encode'.")


# message = decode("J%!% V4t%r")
# message2 = encode("Joao Vitor")

# print(message)
# print(message2)


user_mode = str(input("Type 'encode' to encrypt, type 'decode' to decrypt: "))
user_message = str(input("Type your message: "))  
result = decode_encode(user_message, user_mode)
print(f'The {user_mode}d message is: {result}')

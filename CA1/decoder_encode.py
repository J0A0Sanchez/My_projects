# Task 3 & 4: Decode and Encode function

def decode(text, disc):
    """Decodes a secret message by replacing encoded characters."""
    secret = ""
    for char in text:
        if char in disc:
            secret += disc[char]
        else:
            secret += char
    return secret


def encode(text, disc):
    """Encodes a message using the dictionary."""
    secret = ""
    for char in text:
        if char in disc:
            secret += disc[char]
        else:
            secret += char
    return secret



vowels = {"!": "a", "&": "e", "4": "i", "%": "o", ")": "u"}
vowels_encoded = {v: k for k, v in vowels.items()}

message = decode("J%!% V4t%r", vowels)
message2 = encode("Joao Vitor", vowels_encoded)

print(message)
print(message2)

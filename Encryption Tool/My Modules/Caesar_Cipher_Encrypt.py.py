def caesar_cipher(text, shift, mode='encrypt'):
    result = ""

    if mode == 'decrypt':
        shift = -shift

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt/Decrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt/Decrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char

    return result
# Example usage
text = "Hello, I'm Trevon Swift and I think Cybersecurity is awesome!"
shift = 32

# Encrypt the text
encrypted_text = caesar_cipher(text, shift, mode='encrypt')
print(f"Original Text: {text}")
print(f"Shift: {shift}")
print(f"Encrypted Text: {encrypted_text}")

# Decrypt the text
decrypted_text = caesar_cipher(encrypted_text, shift, mode='decrypt')
print(f"Decrypted Text: {decrypted_text}")

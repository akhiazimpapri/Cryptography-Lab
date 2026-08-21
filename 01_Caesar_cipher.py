
def caesar_cipher(text, shift):
    result = ""
    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            shifted = (ord(c) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += c
    return result

plaintext = "HELLO WORLD"
print("Plaintext:", plaintext)

ciphertext = caesar_cipher(plaintext, 3)
print("Ciphertext:", ciphertext)

text = caesar_cipher(ciphertext, -3)
print("Decrypted Text:", text)
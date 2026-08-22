
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


def encrypt(plaintext, width = 4):
    length = len(plaintext)
    cipher_text = ""

    for k in range(width):
        for i in range(k, length, width):
            cipher_text += plaintext[i]
    
    return cipher_text


def decrypt(cipher_text, width = 4):
    length = len(cipher_text)
    plain_text = [''] * length
    idx = 0

    for k in range(width):
        for i in range(k, length, width): 
            plain_text[i] = cipher_text[idx]
            idx += 1

    return ''.join(plain_text)

plaintext = "Computer Science"
print("Plaintext:", plaintext)

ciphertext = caesar_cipher(plaintext, 3)
print("Ciphertext:", ciphertext)

width = 5
cipher_text = encrypt(ciphertext, width)
print(f"Encrypted Text: {cipher_text}")

decrypted_ciphertext = decrypt(cipher_text, width)
print(f"Decrypted Ciphertext: {decrypted_ciphertext}")

text = caesar_cipher(ciphertext, -3)
print("Decrypted Text:", text)
   
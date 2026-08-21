def encrypt(plain_text, width = 4):
    length = len(plain_text)
    cipher_text = ""

    for k in range(width):
        for i in range(k, length, width):
            cipher_text += plain_text[i]
    
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

plain_text = "Cryptography & Network Security Lab"
width = 7
cipher_text = encrypt(encrypt(plain_text, width), width)
decrypted_text = decrypt(decrypt(cipher_text, width), width)

print(f"Plain Text: {plain_text}")
print(f"Encrypted Text: {cipher_text}")
print(f"Decrypted Text: {decrypted_text}")
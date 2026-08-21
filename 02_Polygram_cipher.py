# Polygram Substitution

block_pairs = "COM XQZ PUT YRT ERS ABC ING QWE THE JKL BAN PLM GLA VNM DES HYT"

words = block_pairs.split()

encryption_rules, decryption_rules = {}, {}

for i in range(0, len(words), 2):
    word1, word2 = words[i], words[i + 1]
    encryption_rules[word1] = word2
    decryption_rules[word2] = word1

print(encryption_rules)  
print(decryption_rules)


def encrypt(plain_text):
    cipher_text = ""
    block = ""

    for i in range(len(plain_text)):
        if i and i % 3 == 0:
            cipher_text += encryption_rules[block]
            block = ""     
        block += plain_text[i]
    
    cipher_text += encryption_rules[block]
    return cipher_text


def decrypt(cipher_text):
    plain_text = ""
    block = ""

    for i in range(len(cipher_text)):
        if i and i % 3 == 0:
            plain_text += decryption_rules[block]
            block = ""     
        block += cipher_text[i]
    
    plain_text += decryption_rules[block]
    return plain_text


plaintext = "COMPUTERSTHEBAN"  

cipher_text = encrypt(plaintext)
decrypted_text = decrypt(cipher_text)

print(f"Plain Text: {plaintext}")
print(f"Encrypted Text: {cipher_text}")
print(f"Decrypted Text: {decrypted_text}")
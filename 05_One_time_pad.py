key = "DFHKAJSDHFAKLDSFJKLDJFLKJFALKDJF"

def encrypt(plaintext):
  ciphertext = ""
  idx = 0
  for m in plaintext:
    x = (ord(m) + ord(key[idx])) % 26
    idx += 1
    ciphertext += chr(ord("A") + x)

  return ciphertext  

def decrypt(ciphertext):
  plaintext = ""
  idx = 0
  for c in ciphertext:
    x = (ord(c) - ord(key[idx])) % 26
    idx += 1
    plaintext += chr(ord('A') + x)

  return plaintext 

plaintext = input("Enter your text to encrypt : ")
encrypt_text = encrypt(plaintext)
decrypt_text = decrypt(encrypt_text)

print("Your plaintext : ", plaintext)
print("Encrypted Text : ", encrypt_text)
print("Decrypted Text ; ", decrypt_text)  
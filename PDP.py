# !pip install pycryptodome
import zlib
import secrets
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA1
from Crypto.Cipher import DES3, PKCS1_OAEP
from Crypto.Util.Padding import pad, unpad

A_private = RSA.generate(1024)
A_public = A_private.public_key()

B_private = RSA.generate(1024)
B_public = B_private.public_key()

print("\nSender side :")

M = b"How are you ?"
print("Original Message : ", M.decode())

H = SHA1.new(M)
S = pkcs1_15.new(A_private).sign(H)
data = len(S).to_bytes(2, "big") + S + M
data = zlib.compress(data)

Ks = DES3.adjust_key_parity(secrets.token_bytes(16))
C = DES3.new(Ks, DES3.MODE_ECB).encrypt(pad(data, DES3.block_size))
E_Ks = PKCS1_OAEP.new(B_public).encrypt(Ks)
packet = (E_Ks, C)

print("Packet Sent")

# Receiver
Ks = PKCS1_OAEP.new(B_private).decrypt(packet[0])

data = DES3.new(Ks, DES3.MODE_ECB).decrypt(packet[1])
data = unpad(data, DES3.block_size)
data = zlib.decompress(data)

n = int.from_bytes(data[:2], "big")
S = data[2:2+n]
M = data[2+n:]

print("Decrypted Message : ", M.decode())

try:
  pkcs1_15.new(A_public).verify(SHA1.new(M),S)
  print("Athentication Provided")
except:
  print("Athentication Failed")
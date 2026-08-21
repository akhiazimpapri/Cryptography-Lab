import random

p = 353
g = 3

print(f"Prime number : {p}")
print(f"Primitive root : {g}")

xa = random.randint(2, p-2)
xb = random.randint(2, p-2)

print(f"Alice's private key : {xa}")
print(f"Bob's private key : {xb}")

ya = pow(g, xa, p)
yb = pow(g, xb, p)

print(f"Alice's public key : {ya}")
print(f"Bob's public key : {yb}")

sectet_a = pow(yb, xa, p)
sectet_b = pow(ya, xb, p)

print(f"Alice's sectet key : {sectet_a}")
print(f"Bob's sectet key : {sectet_b}")

if(sectet_a == sectet_b):
    print("Key exchange successful")
else :
    print("Key are not same")

import random

p = 353
g = 3

print(f"Prime number : {p}")
print(f"Primitive root : {g}")

a = random.randint(2, p-2)
b = random.randint(2, p-2)

print(f"Alice's private key : {a}")
print(f"Bob's private key : {b}")

A = pow(g, a, p)
B = pow(g, b, p)

print(f"Alice's public key : {A}")
print(f"Bob's public key : {B}")

sectet_a = pow(B, a, p)
sectet_b = pow(A, b, p)

print(f"Alice's sectet key : {sectet_a}")
print(f"Bob's sectet key : {sectet_b}")

if(sectet_a == sectet_b):
    print("Key exchange successful")
else :
    print("Key are not same")

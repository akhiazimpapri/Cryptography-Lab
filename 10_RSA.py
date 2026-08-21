import math

def generate_keys():
	p, q = 17, 13
	n = p*q
	phi = (p-1)*(q-1)
	e = 2
	while math.gcd(e,phi)!=1:
		e+=1
	d = pow(e,-1,phi)
	return (e,n),(d,n)

def encryption(public_key, plain_text):
	e,n = public_key
	cipher = []
	for char in plain_text:
		m = ord(char)
		c = pow(m,e,n)
		cipher.append(c)
	return cipher
		
def decryption(private_key, cipher_text):
	d,n = private_key
	m =""
	for c in cipher_text:
		mi = pow(c,d,n)
		m += chr(mi)
	return m
	
if __name__ == "__main__":
	public_key, private_key = generate_keys()
	plain_text = input("Enter the plaintext : ")
	ciphertext = encryption(public_key, plain_text)
	plain_text1 = decryption(private_key, ciphertext)
	
	print(f"ciphertext is : {ciphertext}")
	print(f"decrypted text is: {plain_text1}")
import hashlib
import zlib
import math

def generate_key(p=23,q=17):
	n = p*q
	phi = (p-1)*(q-1)
	
	e = 1
	while math.gcd(e,n)!=1:
		e+=1
	d = pow(e,-1,phi)
	private_key, public_key = (d,n),(e,n)
	return private_key, public_key
	
def hash1(message):
	encoded = message.encode()
	h = hashlib.sha256(encoded)
	return h.hexdigest()
	
def encryption(key, message):
	e, n = key
	ciphertext = []
	for char in (message):
		m = ord(char)
		c = pow(m,e,n)
		ciphertext.append(c)
	return ciphertext
def decryption(key, ciphertext):
	d,n = key
	message = ""
	for c in (ciphertext):
		m = pow(c,d,n)
		m = chr(m)
		message+=m
	return message

if __name__=="__main__":
	private_key, public_key = generate_key()
	
	#sender
	m = "The name of my country is Bangladesh"
	h1 = hash1(m)
	en = encryption(private_key, h1)
	hm = str(en) + "|" + m
	z = zlib.compress(hm.encode())
	print(f"The sending message is : {z}")
	
	#Receiver
	uz = zlib.decompress(z)
	uz = uz.decode()
	signature, msg = uz.split("|")
	print(f"{msg}")
	
	decrypted_signature = decryption(public_key, eval(signature))
	msg_hash = hash1(msg)
	
	print(f"decrypted signature: {decrypted_signature}")
	print(f"Message_hash : {msg_hash}")
	
	if(decrypted_signature==msg_hash):
		print("PGP is successful")
	else:
		print("Wrong")
	
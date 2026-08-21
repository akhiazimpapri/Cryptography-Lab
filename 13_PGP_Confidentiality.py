import hashlib
import zlib
import math

def generate_key(p=23,q=17):
	n = p*q
	phi = (p-1)*(q-1)
	
	e = 1
	while math.gcd(e,phi)!=1:
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

def sym_encryption(data,key):
	cipher = []
	for byte in data:
		cipher.append(byte^key)
	return bytes(cipher)

def sym_decryption(cipher, key):
	plain = []
	for byte in cipher:
		plain.append(byte^key)
	return bytes(plain)
	e
if __name__=="__main__":
	private_key, public_key = generate_key()
	
	#sender
	original_message = "The name of my country is Bangladesh"
	z = zlib.compress(original_message.encode())
	k = 11
	ec = sym_encryption(z,k)
	ep = encryption(public_key,str(k))
	concatenated = str(ec)+"|"+str(ep)
	
	# reciever
	decrypted_compressed_msg, decrypted_pk = concatenated.split("|")
	decrypted_pk = eval(decrypted_pk)
	decrypted_compressed_msg = eval(decrypted_compressed_msg)
	
	dp = decryption(private_key, decrypted_pk)
	dc = sym_decryption(decrypted_compressed_msg, int(dp))
	
	m = zlib.decompress(dc)
	m = m.decode()
	
	print(f"The original message is : {original_message}")
	print(f"the sent message is: {m}")
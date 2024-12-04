import random
import string

chars=string.punctuation + string.digits + string.ascii_letters + " " #string.whitespace
#print(chars)
chars=list(chars)     #list is used to make strings to individual elements
key=chars.copy()
#print(f'chars:{chars}')
#print(f'key:{key}')
random.shuffle(key)    #shuffle the place of key

#ENCRYPTION
plain_text=input("enter the messege to encrypt:")
cipher_text=""

for letter in plain_text:
    index=chars.index(letter)
    cipher_text+=key[index]

print(f"Original messege: {plain_text}")
print(f"Encrypted messege: {cipher_text}")


#DECRYPTION
cipher_text=input("enter the messege to decrypt:")
plain_text=""

for letter in cipher_text:
    index=key.index(letter)
    plain_text+=chars[index]

print(f"Encrypted messege: {cipher_text}")
print(f"Original messege: {plain_text}")

import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters 
chars = list(chars)
key = chars.copy()
random.shuffle(key)

read_text = input("Enter message for encrypt: ")
cipher_text = ""

for letter in read_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"message {read_text}")
print(f"encrypted {cipher_text}")

cipher_text = input("Enter encrypt message: ")
read_text = ""

for letter in cipher_text:
    index = key.index(letter)
    read_text += chars[index]

print(f"encrypted {cipher_text}")
print(f"message {read_text}")

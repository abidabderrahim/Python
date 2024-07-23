import string
import random

characters = list(string.ascii_letters + string.digits+ string.punctuation)

def generate_password():
    password_length = int(input("Password Lenght : "))
    random.shuffle(characters)
    password = []
    for x in range(password_length):
        password.append(random.choice(characters))
    random.shuffle(password)
    password = "".join(password)
    print(password)


generate_password()

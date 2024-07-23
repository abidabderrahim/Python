import os
import random
import string

length = int(input("Enter number of Strings : "))
random_bytes = os.urandom(length)

string_list = []
for i in range(10):
    random_string = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for n in range(length)])
    string_list.append(random_string)

print(string_list)

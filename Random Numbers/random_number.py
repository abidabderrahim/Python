import random

num1 = int(input("Enter start number : "))
num2 = int(input("Enter end number : "))
num3 = int(input("number of random numbers : "))
print("this is your random numbers : ", end="")
for i in range(num3):
    rand = random.randint(num1, num2)
    print(rand, end=" ")
print()

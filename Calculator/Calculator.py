operator = input("Enter an Operator (+ - * / ): ")
num1 = float(input("enter the number1 : "))
num2 = float(input("enter the number2 : "))

if (operator == "+"):
    result = num1 + num2
elif (operator == "-"):
    result = num1 - num2
elif (operator == "*"):
    result = num1 * num2
elif (operator == "/"):
    result = num1 / num2
else:
    print("not valid operator !")

print(f"{round(num1)} {operator} {round(num2)} = {round(result, 3)}")

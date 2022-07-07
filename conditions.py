# user_name = input('Enter your name: ')
# user_age = input('Enter your age: ')
# print("Hello " + user_name + " you are " + user_age)


# num1 = input("Enter a number: " )
# num2 = input("Enter another number: " )


# result = float(num1) + float(num2)
# result = int(num1) + int(num2)
# print(result)


num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num3 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num3)
elif op == "-":
    print(num1 - num3)
elif op == "*":
    print(num1 * num3)     
elif op == "/":
    print(num1 / num3)
else:
    print("Invalid operator")            
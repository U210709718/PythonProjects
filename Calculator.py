print("Welcome to the calculator App!")
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
operation = input("Choose the Operation: ")
if operation == "+":
    print(number1 + number2)
elif operation == "-":
    print(number1 - number2)
elif operation == "/":
    print(number1 / number2)
elif operation == "*":
    print(number1 * number2)


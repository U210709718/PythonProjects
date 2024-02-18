print("Welcome to the Calculator App! ")
number_1 = float(input("Please enter the first number :"))
operator = input("Please enter the Operator: ")
number_2 = float(input("Please enter the second number :"))

if operator == "+":
    print(number_1 + number_2)
elif operator == "-" :
    print(number_1 - number_2)
elif operator == "*" :
    print(number_1 * number_2)
elif operator == "/" :
    print( number_1 / number_2)
else :
    print( "Wrong Operator please try agian !")
# Task 1: Basic Calculator
# Objective:
# Create a Python program that works like a calculator. It should:
# Ask the user to enter two numbers.
# Ask the user to choose an operation: +, -, *, /, //, %, **.
# Perform the selected operation using conditional statements (if-elif-else).
# Display the result using print() with proper formatting.
# Use type casting, arithmetic operators, assignment operators, and input/output.

print(f"Welcome to our calculator")
num1 = int(input("Enter value of number 1 : "))
num2= int(input("Enter value of number 1 : "))
operator=(input("Choose operations : +, -, *, /, //, %, ** : "))[0]

if(operator=='+'):
    print(f"Addition of number1 and number2 = {num1+num2}")
elif (operator=='-'):
    print(f"Subtraction of number1 and number2 = {num1-num2}")
elif (operator=='*'):
    print(f"Multiplication of number1 and number2 = {num1*num2}")
elif (operator=='/'):
    print(f"Division of number1 and number2 = {num1/num2}")
elif (operator=='//'):
    print(f"Floor Division of number1 and number2 = {num1//num2}")
elif (operator=='**'):
    print(f"Exponent of number1 and number2 = {num1**num2}")
else:
    print(f"Enter valid operator")
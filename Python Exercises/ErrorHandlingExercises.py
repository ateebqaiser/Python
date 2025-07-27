# Task 1: Division with Try/Except
# Goal: Use try and except to catch division by zero.
# Task:
# Ask the user to input two numbers. Divide them.
# If the second number is 0, catch the error and print "Division by zero is not allowed!"


num1=int(input("Enter first number = "))
num2=int(input("Enter second number = "))
try:
    print(num1/num2)
except ZeroDivisionError:
    print("Division by zero is not allowed!")
    


# Task 2: Even Number Checker with Else
# Goal: Use try, except, and else
# Task:
# Take a number input from the user.
# Use try to convert it to an integer.
# If successful, check if it's even or odd (in the else block).
# If input is invalid (like "abc"), catch the error and print "Please enter a valid number".


try:
    num=float(input("Enter number = "))
    num1=int(num)
except ValueError:
    print("Please enter a valid number")
else:
    if(num1%2==0):
        print(f"After changing {num} into integer,{num1} is a even number")
    else:
        print(f"After changing {num} into integer,{num1} is a odd number")



# Task 3: Custom Age Validator using raise
# Goal: Use raise
# Task:
# Write a function check_age(age)
# If age < 0, raise an exception:

# raise ValueError("Age cannot be negative")
# Otherwise, print "Valid age"

# Call the function with user input.

def check_age(age):
    if age<0:
        raise ValueError("Age cannot be negative")
    else:
        print("Valid Age")

try:
    age1 = int(input("Enter age = "))
    check_age(age1)
except ValueError as e:
    print("Error:", e)

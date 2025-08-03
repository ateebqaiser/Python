# Task 2: Grading System with Switch & Conditions
# Objective:
# Create a Python program to take a students marks (0 to 100) and:
# Calculate grade using:
# if-elif-else (nested and shorthand where possible)
# Logical operators to handle ranges
# Use a dictionary or match-case to map grades to remarks like:
# A → "Excellent", B → "Good", C → "Average", etc.
# Use variables, type casting, comparison operators, logical operators, and formatted print output.

print(f"Welcome to Grading System")
marks=float(input("Enter student marks between 0-100 : "))
if(marks>=0 and marks<=100):
    if(marks<=100 and marks>=90):
        grade='A'
    elif(marks<90 and marks>=80):
        grade='B'
    elif(marks<80 and marks>=70):
        grade='C'
    elif(marks<70 and marks>=60):
        grade='D'
    elif(marks<60 and marks>=50):
        grade='E'
    else:
        grade='F'
    match grade:
        case 'A':
            print(f"Your grade is {grade} \nRemarks : Excellent")
        case 'B':
            print(f"Your grade is {grade} \nRemarks : Good")
        case 'C':
            print(f"Your grade is {grade} \nRemarks : Average")
        case 'D':
            print(f"Your grade is {grade} \nRemarks : Work Hard")
        case 'E':
            print(f"Your grade is {grade} \nRemarks : Need improvement")
        case _:
            print(f"Your grade is {grade} \nRemarks : Fail,Try Again!")
else:
    print(f"Please Enter marks between 0-100")
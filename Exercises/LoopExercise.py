#Task 1: Table Generator (Loop + String Formatting)
# Topic Covered: while, for, range(), strings
# Task:
# Ask the user for a number and print its multiplication table using a for loop with range().
# 📌 Bonus: Use f-string for formatting (like 2 x 1 = 2).


print("Welcome to table generator")
number=int(input("Enter table number you want to generate = "))
for i in range(1,11):
    print(f"{number} x {i} = {number*i}")

#By using while
i=1
while i<=10:
    print(f"{number} x {i} = {number*i}")
    i+=1

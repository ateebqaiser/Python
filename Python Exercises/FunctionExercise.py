# # Task 1: Simple Greeting Function
# # Topic Covered: def, positional argument
# # Task:
# # Create a function named greet_user(name) that prints a welcome message using the user's name
# # Example Call:
# # greet_user("Ateeb")  # Output: Welcome, Ateeb!

# def greet_user(name="Guest"):
#     print(f"Weclome, {name}!")

# name=input("Enter user name = ")
# greet_user(name)



# #  Task 2: Calculator with Default Operation
# # Topics: def, default argument, return
# # Task:
# # Create a function calculate(num1, num2, operation='add')
# # Return the result based on the operation:
# # If operation == 'add' → return num1 + num2
# # If operation == 'multiply' → return num1 * num2
# # Try calling it with and without passing the third argument



# def calculate(num1,num2,operation="add"):
#     if(operation=="add"):
#         return num1+num2
#     elif(operation=="multiply"):
#         return num1*num2
#     elif(operation=="sub"):
#         return num1-num2
#     elif(operation=="divide"):
#         if(num2==0):
#             print("Divison by 0 is not possible")
#         else:
#             return num1/num2
#     else:
#         print("Invalid Operation")
    
# num1=int(input("Enter number 1 = "))
# num2=int(input("Enter number 2 = "))
# operation=input('Enter operation = ')
# result=calculate(num1,num2,operation)
# print(f"Result = {result}")


# # Task 3: Add All Using args
# # Topics: *args, loop
# # Task:
# # Create a function add_all(*numbers)
# # It should add all numbers passed and print the total.
# # Example call:
# # add_all(1, 2, 3, 4)   # Output: Total is 10


# def add_all(*numbers):
#     sum=0
#     for num in numbers:
#         sum+=num
#     return sum,len(numbers)

# total,count= add_all(1,2,3,4,5)
# print(f"Addition of all numbers = {total}")
# print(f"Total numbers that was added {count}")



# Task 4: Show Details Using kwargs
# Topics: **kwargs, loop
# Task:
# Create a function show_details(**info)
# It should print each key and value like:
# name: Ateeb  
# age: 20  
# city: Lahore

def show_details(**info):
    for key,value in info.items():
        print(f"{key}:{value}")

name1=input("Enter name = ")
age1=int(input("Enter age = "))
city1=input("Enter city = ")
print("Details: ")
show_details(name=name1,age=age1,city=city1)
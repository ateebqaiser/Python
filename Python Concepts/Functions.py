#Defining a Function
#Syntax:
#def function_name(parameters):
    # code block

def greeting():
    print("Hello world")

greeting()


#Parameters and Arguments

#Positional Arguments (in order)
def studentdata(name,age):
    print(f"Student name : {name} and his age {age}")

studentdata("Ateeb",20) #order matters

#Keyword Arguments (name=value)
studentdata(age=20, name="Ateeb")  # order doesn't matter

#Default Parameters
def greet(name="Guest"):
    print(f"Welcome, {name}")

greet()             # Output: Welcome, Guest
greet("Ateeb")      # Output: Welcome, Ateeb

#Return Statement
def add(a, b):
    return a + b

# result = add(3, 4)
#print("Sum:", result)
print("Sum:", add(3,4))

#*args (Multiple Positional Arguments) *args collects all extra positional arguments into a tuple.
def total(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    print("Total:", sum)

total(1, 2, 3, 4)   # Total: 10
total(5, 10)        # Total: 15

#**kwargs (Multiple Keyword Arguments) **kwargs collects keyword arguments into a dictionary
def student_info(**data):
    for key, value in data.items():
        print(f"{key}: {value}")


student_info(name="Ateeb", age=20, grade="A")

def profile(name, *skills, **details):
    print(f"Name: {name}")
    print("Skills:", skills)
    print("Details:", details)

profile("Ateeb", "Python", "C++", age=20, city="Lahore")





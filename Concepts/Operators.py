# Arthimetic operators   (+, -, *, /, //, %, **)

a = 5
b = 7
add = a+b

print (f"Additon of a and b = {add}")
print (f"Sqaure root of {a} = {a**2}")
print (f"Subtraction of a and b = {a-b}")
print (f"Multipication of a and b = {a*b}")
print (f"Division of a and b = {a/b}")
print (f"Floor Division of a and b = {a//b}")
print (f"Reminder of a and b = {a%b}")


#Relational/Comparison Operators (==, !=, <, >, <=, >=)

print (a!=b)
print (a>b)
print (a>=b)
print (a<b)
print (a<=b)

#Logical Operators (and, or, not)
print (a<b and b<a)
print (a<b  or b<a)
print (not(b<a))


#Assignment Operators (*=,+=,-=)

c=10
c+=20    #c*=20  c-=20  c=c+20
print(c) 

#Identity Operators(is,is not)
# Identity operators check whether two variables refer to the same object in memory

a=10
b=10
print(a is b)
print(a is not b)

#Membership operator (in,not in)
# in → Checks if a value exists in a sequence (like list, string, tuple, set, or dictionary keys)
#not in → Checks if a value does NOT exist in a sequence

fruits = ["apple", "banana", "mango"]

print("apple" in fruits)       # True → apple is in the list
print("grapes" in fruits)      # False → grapes is not in the list
print("banana" not in fruits)  # False → banana is in the list

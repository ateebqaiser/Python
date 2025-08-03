#Conditional Statements (if, else, elif)

x=20
y=30

#if:
if(x<y):
    print(f"x is less than y")

#if-else:
if(x>y):
    print(f"x is greater than y")
else:
    print(f"y is greater than x")

#if-elif-else:
if(x==y):
    print(f"x is equal to y")
elif(x<y):
    print(f"x is less than y")
else:
    print(f"x is greater than y")


#Nested Conditions:
z = 10

if z> 5:
    if z < 15:
        print("Between 5 and 15")
    else:
        print("More than 15")
else:
    print("5 or less")


#Short-hand If Expression (One-liners)
a = 10
b = 5

# Single if
if a > b: print("a is greater")

# if-else in one line
print("a" if a > b else "b")  # Output: a


#for switch use match
value = 2

match value:
    case 1:
        print("One")
    case 2:
        print("Two")
    case _:
        print("Other")

# case _: (default)

value2 = 'a'

match value2:
    case 'a':
        print("One")
    case 'b':
        print("Two")
    case _:
        print("Other")

#switch by dictionary:
def day_name(day_num):
    return {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday"
    }.get(day_num, "Invalid Day")

print(day_name(2))  # Output: Tuesday
print(day_name(5))  # Output: Invalid Day

# Task 3: Data Filter with break, continue, and set
# Topic Covered: set, loop, break, continue
# Task:
# Create a set of integers from 1 to 20.
# Use a for loop to print only the even numbers, but:
# continue if the number is divisible by 3
# break if the number reaches 16

print("Welcome to Data filter")

int_numbers=set(range(1,21))
for num in sorted(int_numbers):
#for num in {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}:
    if(num % 2 == 0):
        if(num % 3 == 0):
            continue
        print(num)
        if(num==16):
            break

# Task 4: Tuple & String Practice
# Topic Covered: tuple, string slicing, pass
# Task:
# Create a tuple of 5 fruits.
# Use a for loop to print only those fruits that start with 'a' or 'A'.
# If none match, just pass.


fruits=("Apple","Bananna","Orange","abiu","Mango")
for i in fruits:
    if (i[0]=='A' or i[0]=='a'):
        print(i)
    else:
        pass


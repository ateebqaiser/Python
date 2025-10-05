# List Operations — Normal & Nested Lists with Definitions

# 1. Creation
# Create a list with elements (normal or nested).

normal = [1, 2, 3, 4]
nested = [[1, 2], [3, 4], [5, 6]]

print("Normal:", normal)
print("Nested:", nested)

# 2. Access Elements
#Access elements by index (start from 0). Nested: access inside sublists.**

print(normal[0])       # 1 (first element)
print(normal[-1])      # 4 (last element)

print(nested[0])       # [1, 2] (first sublist)
print(nested[1][1])    # 4 (second element in second sublist)

# 3. Modify Elements
# Change elements by index. Nested: modify inside sublists.

normal[0] = 100
print(normal)          # [100, 2, 3, 4]

nested[0][1] = 200
print(nested)          # [[1, 200], [3, 4], [5, 6]]

# 4. Append / Insert Elements
# Add element at end (append) or at specific index (insert). Nested: append inside sublists.

normal.append(5)
print(normal)          # [100, 2, 3, 4, 5]

nested[1].append(50)
print(nested)          # [[1, 200], [3, 4, 50], [5, 6]]

normal.insert(2, 999)
print(normal)          # [100, 2, 999, 3, 4, 5]

nested.insert(1, [7, 8])
print(nested)          # [[1, 200], [7, 8], [3, 4, 50], [5, 6]]

# 5. Delete / Remove Elements
# Delete by index (del), remove first occurrence by value (remove), or remove and return last or given index element (pop).**

del normal[1]          
print(normal)          # [100, 999, 3, 4, 5]

normal.remove(999)     
print(normal)          # [100, 3, 4, 5]

val = normal.pop()     
print(val)             # 5
print(normal)          # [100, 3, 4]

del nested[2][0]       # delete element inside sublist
print(nested)          # [[1, 200], [7, 8], [4, 50], [5, 6]]

# 6. Extend Lists
# Add all elements of one list to another (like append many at once). Nested: extend sublist with multiple elements.**

a = [1, 2]
b = [3, 4]
a.extend(b)
print(a)               # [1, 2, 3, 4]

nested[0].extend([999, 1000])
print(nested)          # [[1, 200, 999, 1000], [7, 8], [4, 50], [5, 6]]

# 7. Length
# Get number of elements in list (normal or nested). For nested, len() returns number of sublists.**

print(len(normal))     # e.g. 5
print(len(nested))     # e.g. 4 (number of sublists)
print(len(nested[0]))  # length of first sublist, e.g. 4

# 8. Sorting
# Sort elements in ascending or descending order. For nested, sort by key inside sublists.**

lst = [3, 1, 4, 2]
lst.sort()
print(lst)             # [1, 2, 3, 4]

nested = [[3, 2], [1, 5], [4, 0]]
nested.sort(key=lambda x: x[0])  
print(nested)          # [[1, 5], [3, 2], [4, 0]]

# 9. Reverse & Clear
# Reverse list in place or remove all elements.**

normal.reverse()
print(normal)          # reversed list

nested[0].reverse()
print(nested)          # reversed first sublist

normal.clear()
print(normal)          # empty list []

nested.clear()
print(nested)          # empty list []


# 10. Copy (Shallow)
# Make a shallow copy (new list, but nested sublists are shared).**

normal = [1, 2, 3]
normal_copy = normal.copy()

nested = [[1, 2], [3, 4]]
nested_copy = nested.copy()

print(normal_copy)     # [1, 2, 3]
print(nested_copy)     # [[1, 2], [3, 4]]

nested_copy[0][0] = 999  
print(nested)          # [[999, 2], [3, 4]] — original changed (shared sublist)

# 11. Count & Index
# Count occurrences of a value and find first index of a value. Works for nested sublists too (exact match).**

lst = [1, 2, 2, 3]
print(lst.count(2))    
print(lst.index(2))    

nested = [[1, 2], [3, 4], [1, 2]]
print(nested.index([1, 2]))  # 0 (first matching sublist)

# 12. Membership Test
# Check if value or sublist exists in list.**

print(2 in normal)     
print([1, 2] in nested)

# 13. List Comprehensions
# Create new lists easily using loops and conditions. Flatten nested lists or filter sublists.**

squares = [x**2 for x in range(5)]  
print(squares)           # [0, 1, 4, 9, 16]

flat = [item for sublist in nested for item in sublist]  
print(flat)              # flatten nested list

filtered = [sub for sub in nested if sum(sub) > 3]  
print(filtered)          # sublists with sum > 3

# 14. Zip Two Lists
# Pair elements from two lists into tuples. Works element-wise for nested lists too.**

a = [1, 2, 3]
b = ['a', 'b', 'c']
zipped = list(zip(a, b))
print(zipped)            # [(1, 'a'), (2, 'b'), (3, 'c')]

nested_a = [[1, 2], [3, 4]]
nested_b = [['a', 'b'], ['c', 'd']]
zipped_nested = [list(zip(x, y)) for x, y in zip(nested_a, nested_b)]
print(zipped_nested)     # [[(1, 'a'), (2, 'b')], [(3, 'c'), (4, 'd')]]

# 15. Repeat Elements (Multiplication)
# Create a list with repeated elements. For nested lists, beware shared references.**

lst = [0] * 5
print(lst)              # [0, 0, 0, 0, 0]

nested = [[1, 2]] * 3
print(nested)           # [[1, 2], [1, 2], [1, 2]]

nested[0][0] = 99
print(nested)           # all sublists changed because same reference!

#Bonus: Remove Duplicates
# Remove duplicates from normal list using set (order not guaranteed). For nested lists, manually check for duplicates.**

lst = [1, 2, 2, 3, 4, 4]
unique = list(set(lst))
print(unique)

nested = [[1, 2], [3, 4], [1, 2]]

unique_nested = []
for sub in nested:
    if sub not in unique_nested:
        unique_nested.append(sub)

print(unique_nested)


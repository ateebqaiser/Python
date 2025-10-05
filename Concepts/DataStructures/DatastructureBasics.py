#Strings (Immutable, slicing, functions)
name="Ateeb"
print(name)



#Immutable means: You can’t change characters in a string directly. 
#name = "Ateeb"
# name[0] = 'B'   ❌ Error! Strings can't be changed like this.

new_name = "B" + name[1:]
print(new_name)      # Bteeb

new_name2 = name[:4]+"q"
print(new_name2)      # Ateeq

new_name3 = name[:3]+"k"+name[4:]
print(new_name3)      # Atekb



#string slicing
s = "Python"
print(s[0])       # P
print(s[1:4])     # yth
print(s[:3])      # Pyt
print(s[2:])      # thon
print(s[::-1])    # Reverse → nohtyP 
print(s[::-2])    # nhy (2 jumps)



# String Concatenation & Repetition
first_name="Ateeb"
last_name="Qaiser"
print(f"My full name is {first_name+" "+last_name}")
print(f"Repeat my name 3 times {"Ateeb " *3} ")



#Loop through a String
for names in "Ateeb":
    print(names)




# | Function       | Description                     | Example                            | Output            |
# | -------------- | ------------------------------- | ---------------------------------- | ----------------- |
# | `len()`        | Length of string                | `len("Ateeb")`                     | `5`               |
# | `upper()`      | All uppercase                   | `"abc".upper()`                    | `'ABC'`           |
# | `lower()`      | All lowercase                   | `"XYZ".lower()`                    | `'xyz'`           |
# | `capitalize()` | Capitalize first letter         | `"python".capitalize()`            | `'Python'`        |
# | `title()`      | Capitalize each word            | `"ateeb qaiser".title()`           | `'Ateeb Qaiser'`  |
# | `strip()`      | Remove spaces (start & end)     | `" hello ".strip()`                | `'hello'`         |
# | `replace()`    | Replace part of string          | `"Hi John".replace("John", "Ali")` | `'Hi Ali'`        |
# | `find()`       | Find index of a substring       | `"apple".find("p")`                | `1`               |
# | `count()`      | Count occurrences of substring  | `"banana".count("a")`              | `3`               |
# | `split()`      | Split by space (or char)        | `"a,b,c".split(",")`               | `['a', 'b', 'c']` |
# | `join()`       | Join list with string           | `" ".join(['I', 'am', 'GPT'])`     | `'I am GPT'`      |
# | `isdigit()`    | Check if string has only digits | `"123".isdigit()`                  | `True`            |
# | `isalpha()`    | Check if only alphabets         | `"abc".isalpha()`                  | `True`            |



#Lists
#Ordered, Mutable (you can change items)
fruits = ["apple", "banana", "cherry",1]
fruits.append("orange")     # add item
fruits[1] = "mango"         # change item
print(fruits)               # ['apple', 'mango', 'cherry', 1,'orange']



#Tuples
#Ordered, Immutable
point = (10, 20)
print(point[0])        # 10

# point[0] = 50        ❌ Error (cannot modify tuple)



#Sets
#Only unique elements , Useful for removing duplicates
nums = {1, 2, 3, 2, 1}
print(nums)              # {1, 2, 3}

nums.add(0)
nums.remove(2)
print(nums)              # {0, 3, 4}



#Dictionaries 
#Key-Value pairs ,Keys must be unique
student = {
    "name": "Ateeb",
    "age": 20,
    "grade": "A"
}

print(student["name"])      # Ateeb
student["age"] = 21         # update value
print(student.get("grade", "N/A"))  # N/A


studentdata ={
    "names":["Ateeb","Ali"],
    "semester": [1,2,3,4],
    "grade":["A","A+"]
}

print(f"Names of topper students : {studentdata["names"][0]} from semester {studentdata["semester"][3]} and he get {studentdata["grade"][0]}")
print(f"Names of Fail students : {studentdata["names"][1]} from semester {studentdata["semester"][1]} and he get {studentdata.get("grade","F")}")




# for comment we use hashtag

#Variable decelartion & initialization
name = "Ateeb" # for string data
age = 20  # for integer data
height = 5.7 # for real data
married = True # for bool data
gender = 'M' # for character data

#Identify variable datatype
print("Name : ", type(name))
print("Age : ",type(age))
print("Height : ",type(height))
print("Gender : ",type(gender))
print("Married : ",type(married))

# Output
print("Name : ",name)
print("Age : ",age)
print("Height : ",height)
print("Gender : ",gender)
print("Married : ",married)

#input
father_name = input("Enter your father name : ")
father_age = int(input("Enter your father age : "))
father_height = float(input("Enter your father height : "))
father_married = bool(input("Is your father married : "))
father_gender = (input("Enter your father gender : "))[0]

print(f"My father name is {father_name} and his age is {father_age},height is {father_height},married : {father_married}.")
print(f"Father Gender : {father_gender}")

#Type casting

students_str="100"
students_int=int(students_str)
print(students_int+50)

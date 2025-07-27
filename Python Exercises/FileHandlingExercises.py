# Task 1: Write to a File
# Goal: Use w mode to write data to a file.
# Task:
# Create a file named info.txt
# Ask the user to enter their name and city.
# Write both into the file in this format:
#     Name: Ateeb
#     City: Lahore


# with open("info.txt","w") as file:
#     name=input("Enter name = ")
#     city=input("Enter city = ")
#     file.write(f"Name: {name}\nCity: {city}")    




# Task 2: Read and Display File Content
# Goal: Use r mode and with open() syntax.
# Task:
# Open the info.txt file you created in Task 1,
# Read and print its content line by line.


# with open("info.txt","r") as file:
#     data = file.read()
#     print(data)




# Task 3: Append More Data
# Goal: Use a mode to add more entries.
# Task:
# Ask the user to enter another name and city.
# Append that info to the existing info.txt file
# without overwriting previous content.

# print("Enter two student data")
# for i in range(1,3):
#     name=input(f"Enter {i} student name = ")
#     city=input(f"Enter {i} city name = ")
#     with open ("info.txt","a") as file:
#         file.write(f"Name = {name} \nCity = {city}\n\n")




# Task 4: Read and Update using r+
# Goal: Use r+ mode (read + write)
# Task:
# Open info.txt using r+,
# Read and display the content,
# Then overwrite the file from the beginning with this message:

#             File Overwritten Successfully.

with open("info.txt","r+") as file:
    content=file.read()
    print(content)
    file.seek(0)        #it moves the cursor to the nth byte (or character for text files) in the file.
    file.write("File Overwritten Successfully.")
    file.truncate() # remove leftover content if any
    print("File Overwritten Successfully.")


# Example: Delete Line Containing "Ali"

with open("info.txt", "r") as file:
    lines = file.readlines()

with open("info.txt", "w") as file:
    for line in lines:
        if "Ali" not in line:
            file.write(line)
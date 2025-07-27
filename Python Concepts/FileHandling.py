# 1. Basic Syntax

# file = open("filename.txt", "mode")
# # do something
# file.close()

# 2. with open() as (Best Practice)
    
with open("file.txt", "r") as file:
    content = file.read()

# 3. File Modes

# | Mode   | Meaning                 | Use Case                    |
# | ------ | ----------------------- | --------------------------- |
# | `'r'`  | Read only (default)     | File **must exist**         |
# | `'w'`  | Write (overwrites file) | Creates file if not exist   |
# | `'a'`  | Append (adds at end)    | Keeps old content, adds new |
# | `'r+'` | Read + Write            | File **must exist**         |

# 4. Reading from File

with open("file.txt", "r") as file:
    data = file.read()
    print(data)

# output:
# Hello Ateeb

# 5. Writing to File (w mode)  This will overwrite any old content.

with open("file.txt", "w") as file:
    file.write("Welcome, Ateeb!")

 

# 6. Appending to File (a mode)  Adds new line without removing old content.

with open("file.txt", "a") as file:
    file.write("\nNew line added.")



# 7. Read + Write (r+ mode)

with open("file.txt", "r+") as file:
    old = file.read()
    file.write("\nAppended using r+")

#seek and trncate


with open("info.txt","r+") as file:
    content=file.read()
    print(content)
    file.seek(0)        #it moves the cursor to the nth byte (or character for text files) in the file.
    file.write("File Overwritten Successfully.")
    file.truncate() # remove leftover content if any
    print("File Overwritten Successfully.")


# Basic try-except

# try: Jahan hum risk wala code likhte hain
# except: Agar error aaye to yahaan Python catch karta hai aur message print karta hai

try:
    num = int(input("Enter a number: "))
    print(10 / num)
except:
    print("Error: Invalid number or divide by zero.")

# If input = 2 :  5.0
# If input = 0 or abc :  ❌ Error: Invalid number or divide by zero.


try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ZeroDivisionError:
    print("❌ You can't divide by zero.")
except ValueError:
    print("❌ Please enter a valid number.")

# Input = 5 : 2.0
# Input = 0 : You can't divide by zero.
# Input = hello : ❌ Please enter a valid number.




# else and finally block

# else: Agar koi error na aaye, to ye chalega (optional)
# finally: Ye block hamesha chalta hai (error aaye ya na aaye)


try:
    a = int(input("Enter a number: "))
    print(100 / a)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print("✅ Division successful.")
finally:
    print("🔚 End of operation.")

# Input = 10
# 10.0
# ✅ Division successful.
# 🔚 End of operation.

# Input = 0
# Error: Cannot divide by zero.
# 🔚 End of operation.



# Raise Exception (Custom Error) (Apna khud ka error)

# raise: Agar koi condition galat ho to hum khud Python ko bolo ke error do.


age = int(input("Enter your age: "))
if age < 0:
    raise ValueError("❌ Age can't be negative!")
else:
    print("Age is valid")


# Input = 20
# Age is valid

# Input = -5
# Traceback (most recent call last):
# ...
# ValueError: ❌ Age can't be negative!

# | Error Type          | Kab hoti hai?                       |
# | ------------------- | ----------------------------------- |
# | `ValueError`        | Galat data type (e.g. "abc" in int) |
# | `ZeroDivisionError` | 0 se divide karo                    |
# | `TypeError`         | Galat data type operation           |
# | `FileNotFoundError` | File nahi mili                      |
# | `IndexError`        | List index limit se bahar           |


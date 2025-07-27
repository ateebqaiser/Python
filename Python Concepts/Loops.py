#while Loop

i = 1
while i<=5:
    print(f"Value from 1 to 5 : {i}")
    i+=1 

i=1
while i<=10:
    print(f"2 x {i} = {2*i}")
    i+=1

#for Loop with range()
for i in range(1,6):
    print(i)

#increment
for i in range(1,6,2):
    print(i)

#for loop revese(decrement)
for i in range(6,1,-1):
    print(i)


#break statement
for i in range(1,10):
    if i==9:
        print("All numbers display from 1 to 8")
        break
    print(i)

#continue statement (for 1 skip) 
for i in range(1,10):
    if i==7:
        print("Sorry number 7 not print")
        continue
    print(i)

for students in ("ateeb","zain","ali"):
    if students=="zain":
        continue
    print(f"Present : {students}")
    
#pass statement
for i in range(1,10):
    if i==8:
        pass
    print(i)


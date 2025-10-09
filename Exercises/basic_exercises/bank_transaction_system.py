balance=int(input("Enter account balance : "))
total_balance=balance
option=True
while option==True:
    print("What type of transaction you want : ")
    print("Press 1 for Deposit")
    print("Press 2 for Withdraw")
    print("Press 3 for Check Balance")
    print("Press 4 for Exit")
    choice = int(input("Enter yout choice : "))
    if choice==1:
        deposit=int(input("Enter Deposit amount : "))
        total_balance+=deposit
        print("Deposit successfully done")
        print(f"New Balance : {total_balance}")
    elif choice==2:
        with_draw=int(input("Enter Withdraw amount : "))
        if with_draw<0:
            print("Please enter positive amount")
        else:
            print("Withdraw successfully done")
            total_balance-=with_draw
            print(f"New Balance : {total_balance}")
    elif choice==3:
        print(f"Total Balance : {total_balance}")
    else:
        option=False
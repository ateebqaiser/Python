test_score=float(input("Enter student's test score: "))
interview_score=float(input("Enter student's interview score: "))
sports_quota=input("Does the student have a sports quota? (y/n): ")[0]
if test_score>=70:
    if interview_score>=7:
        if sports_quota=='y' or sports_quota=='Y':
            print("Admitted with sports quota")
        else:
            print("Admitted on merit")
    else:
        if sports_quota=='y' or sports_quota=='Y':
            print("Admitted through sports quota (interview low)")
        else:
            print("Rejected due to low interview score")
elif test_score<70:  
    if sports_quota=='y' or sports_quota=='Y' and test_score>=60:
        print("Admitted via sports quota (borderline case).")
    else:
        print("Not eligible for admission")
    
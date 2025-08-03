import time
import os
from datetime import datetime

#Main Menu
def mainMenu():
    clearscreen()
    if not os.path.exists("students.txt"):
        with open("students.txt","w") as file:
            pass
    while True:
        print("\t--------Welcome to Student Record Manager--------")
        print("1. Admin Panel \n2. Student Panel \n3. Exit")
        choice=valid_intInput("Enter your choice = ")
        match choice:
            case 1:
                adminPanel()
                break
            case 2:
                studentPanel()
                break
            case 3:
                Exit()
                break
            case _:
                invalidOption()
                
#Admin Panel
def adminPanel():
    clearscreen()
    if not os.path.exists("adminCredentials.txt"):
        with open("adminCredentials.txt","w") as file:
            file.write("Fa2023/Ateeb,afv8733")
            pass
    print("\t--------Welcome to Admin Dashboard--------")
    username=valid_stringInput("Enter Username = ")
    password=valid_stringInput("Enter Password = ")
    with open("adminCredentials.txt","r") as file:
        adminData=file.read().split(',')
    if(username == adminData[0] and password == adminData[1]):
        admindashboard()
    else:
        wrongCredentials()
             
#Admin Dashboard
def admindashboard():
    clearscreen()
    while True:
        print("\t--------Welcome to Admin Panel--------")
        print("1.View Student \n2.Add new Student \n3.Update Student Info \n4.Delete Student \n5.Search Student" \
        "\n6.Filter Students\n7.Reset Records \n8.Change Admin Password \n9.Logout")
        adminChoice=valid_intInput("Enter your choice = ")
        match adminChoice:
            case 1:
                viewStudent()
                break
            case 2:
                addStudent()
                break
            case 3:
                updateStudent()
                break
            case 4:
                deleteStudent()
                break
            case 5:
                searchStudent()
                break
            case 6:
                filterStudent()
                break
            case 7:
                resetRecords()
                break
            case 8:
                changePassword()
                break
            case 9:
                logOut()
                break
            case _:
                invalidOption()
            

#View Students (Admin Dashboard)
def viewStudent():
    clearscreen()
    while True:
        print("1.View Records by Semester/Section\n2.View all Male Students\n3.View all Female Students\n4.View All Students\n5.Back to Admin Dashboard")
        viewStudentChoice=valid_intInput("Enter your choice = ")
        match viewStudentChoice:
            case 1:
                viewbySemesterandSection()
            case 2:
                maleStudents()
                break
            case 3:
                femaleStudents()
                break
            case 4:
                allStudents()
                break
            case 5:
                admindashboard()
                break
            case _:
                invalidOption()

#View Records by Semester/Section
def viewbySemesterandSection():
    clearscreen()
    with open("students.txt","r") as viewfile:
        studentRecords=viewfile.readlines()
        if not studentRecords:
            print("No Records found\n")
            returnBackView()
        #For sort
        studentRecords.sort(key=lambda records: records.split(',')[0])
        semester=valid_charInput("Enter Semester (1-8) = ",['1','2','3','4','5','6','7','8'])
        section=valid_charInput("Enter Section (A/B/C/D/E/F/G)= ",['A','B','C','D','E','F','G'])
        total=total1=total2=0

        print(f"Record of {semester}-{section}")
        for line in studentRecords:
            studentRecordData=line.strip().split(',')
            if (studentRecordData[11]==semester and studentRecordData[12]==section ):
                total+=1
                if (studentRecordData[5]=='M'):
                    total1+=1
                elif (studentRecordData[5]=='F'):
                    total2+=1
                print(f"\t--------ID({studentRecordData[0]})--------")
                print(f"Id Password : {studentRecordData[1]}")
                print(f"Name : {studentRecordData[2]}")
                print(f"Father Name : {studentRecordData[3]}")
                print(f"Age : {studentRecordData[4]}")
                print(f"Gender : {studentRecordData[5]}")
                print(f"DOB : {studentRecordData[6]}")
                print(f"Contact No : {studentRecordData[7]}")
                print(f"E-mail : {studentRecordData[8]}")
                print(f"Address : {studentRecordData[9]}")
                print(f"Admission Date : {studentRecordData[10]}")
                print(f"Semester : {studentRecordData[11]}")
                print(f"Section : {studentRecordData[12]}")
                print(f"Total Marks : {studentRecordData[13]}")
                print(f"Percentage : {studentRecordData[14]}%")
                print(f"CGPA : {studentRecordData[15]}")
                print(f"Advance Database : {studentRecordData[16]},{studentRecordData[17]}")
                print(f"Theory of Automata : {studentRecordData[18]},{studentRecordData[19]}")
                print(f"Probability and Statistics : {studentRecordData[20]},{studentRecordData[21]}")
                print(f"Analysis of Algorithm : {studentRecordData[22]},{studentRecordData[23]}")
                print(f"Expository Writing : {studentRecordData[24]},{studentRecordData[25]}")
                print(f"Introduction to Management : {studentRecordData[26]},{studentRecordData[27]}\n")
                
                
        
    print(f"Total Students in {semester}-{section} = {total}")
    print(f"Total Male Students in {semester}-{section} = {total1}")
    print(f"Total Female Students in {semester}-{section} = {total2}\n")
    returnBackView()

#Male Students (View Students)
def maleStudents():
    clearscreen()
    with open("students.txt","r") as viewfile:
        studentRecords=viewfile.readlines()
        if not studentRecords:
            print("No Records found\n")
            returnBackView()
        #For sort
        studentRecords.sort(key=lambda records: records.split(',')[0])
        totalMale=0
        for line in studentRecords:
            studentRecordData=line.strip().split(',')
            if (studentRecordData[5]=='M'):
                totalMale+=1
                print(f"\t--------ID({studentRecordData[0]})--------")
                print(f"Id Password : {studentRecordData[1]}")
                print(f"Name : {studentRecordData[2]}")
                print(f"Father Name : {studentRecordData[3]}")
                print(f"Age : {studentRecordData[4]}")
                print(f"Gender : {studentRecordData[5]}")
                print(f"DOB : {studentRecordData[6]}")
                print(f"Contact No : {studentRecordData[7]}")
                print(f"E-mail : {studentRecordData[8]}")
                print(f"Address : {studentRecordData[9]}")
                print(f"Admission Date : {studentRecordData[10]}")
                print(f"Semester : {studentRecordData[11]}")
                print(f"Section : {studentRecordData[12]}")
                print(f"Total Marks : {studentRecordData[13]}")
                print(f"Percentage : {studentRecordData[14]}%")
                print(f"CGPA : {studentRecordData[15]}")
                print(f"Advance Database : {studentRecordData[16]},{studentRecordData[17]}")
                print(f"Theory of Automata : {studentRecordData[18]},{studentRecordData[19]}")
                print(f"Probability and Statistics : {studentRecordData[20]},{studentRecordData[21]}")
                print(f"Analysis of Algorithm : {studentRecordData[22]},{studentRecordData[23]}")
                print(f"Expository Writing : {studentRecordData[24]},{studentRecordData[25]}")
                print(f"Introduction to Management : {studentRecordData[26]},{studentRecordData[27]}\n")
            
        print(f"Total Male Students = {totalMale}\n")
    returnBackView()

#Female Students (View Students)
def femaleStudents():
    clearscreen()
    with open("students.txt","r") as viewfile:
        studentRecords=viewfile.readlines()
        if not studentRecords:
            print("No Records found\n")
            returnBackView()
        #For sort
        studentRecords.sort(key=lambda records: records.split(',')[0])
        totalFemale=0
        for line in studentRecords:
            studentRecordData=line.strip().split(',')
            if (studentRecordData[5]=='F'):
                totalFemale+=1
                print(f"\t--------ID({studentRecordData[0]})--------")
                print(f"Id Password : {studentRecordData[1]}")
                print(f"Name : {studentRecordData[2]}")
                print(f"Father Name : {studentRecordData[3]}")
                print(f"Age : {studentRecordData[4]}")
                print(f"Gender : {studentRecordData[5]}")
                print(f"DOB : {studentRecordData[6]}")
                print(f"Contact No : {studentRecordData[7]}")
                print(f"E-mail : {studentRecordData[8]}")
                print(f"Address : {studentRecordData[9]}")
                print(f"Admission Date : {studentRecordData[10]}")
                print(f"Semester : {studentRecordData[11]}")
                print(f"Section : {studentRecordData[12]}")
                print(f"Total Marks : {studentRecordData[13]}")
                print(f"Percentage : {studentRecordData[14]}%")
                print(f"CGPA : {studentRecordData[15]}")
                print(f"Advance Database : {studentRecordData[16]},{studentRecordData[17]}")
                print(f"Theory of Automata : {studentRecordData[18]},{studentRecordData[19]}")
                print(f"Probability and Statistics : {studentRecordData[20]},{studentRecordData[21]}")
                print(f"Analysis of Algorithm : {studentRecordData[22]},{studentRecordData[23]}")
                print(f"Expository Writing : {studentRecordData[24]},{studentRecordData[25]}")
                print(f"Introduction to Management : {studentRecordData[26]},{studentRecordData[27]}\n")
                
    print(f"Total Female Students = {totalFemale}\n")
    returnBackView()

#All Students (View Students)
def allStudents():
    clearscreen()
    with open("students.txt","r") as viewfile:
        studentRecords=viewfile.readlines()
        if not studentRecords:
            print("No Records found\n")
            returnBackView()
        #For sort
        studentRecords.sort(key=lambda records: records.split(',')[0])
        total=0
        for line in studentRecords:
            total+=1
            studentRecordData=line.strip().split(',')
            print(f"\t--------ID({studentRecordData[0]})--------")
            print(f"Id Password : {studentRecordData[1]}")
            print(f"Name : {studentRecordData[2]}")
            print(f"Father Name : {studentRecordData[3]}")
            print(f"Age : {studentRecordData[4]}")
            print(f"Gender : {studentRecordData[5]}")
            print(f"DOB : {studentRecordData[6]}")
            print(f"Contact No : {studentRecordData[7]}")
            print(f"E-mail : {studentRecordData[8]}")
            print(f"Address : {studentRecordData[9]}")
            print(f"Admission Date : {studentRecordData[10]}")
            print(f"Semester : {studentRecordData[11]}")
            print(f"Section : {studentRecordData[12]}")
            print(f"Total Marks : {studentRecordData[13]}")
            print(f"Percentage : {studentRecordData[14]}%")
            print(f"CGPA : {studentRecordData[15]}")
            print(f"Advance Database : {studentRecordData[16]},{studentRecordData[17]}")
            print(f"Theory of Automata : {studentRecordData[18]},{studentRecordData[19]}")
            print(f"Probability and Statistics : {studentRecordData[20]},{studentRecordData[21]}")
            print(f"Analysis of Algorithm : {studentRecordData[22]},{studentRecordData[23]}")
            print(f"Expository Writing : {studentRecordData[24]},{studentRecordData[25]}")
            print(f"Introduction to Management : {studentRecordData[26]},{studentRecordData[27]}\n")
       
    print(f"Total Students = {total}\n")
    returnBackView()
            

#Add Student(Admin Dashboard)
def addStudent():
    clearscreen()
    while True:
        student_id=valid_intInput("Enter Student ID = ")
        if duplicateStudent(student_id):
            print("This Student ID already exits. Try again with a new id")
            continue
        else:
            break
    studentPassword=valid_charInput("Do you want to enter new password (Y/N) = ",['Y','N'])
    if(studentPassword=='Y'):
        newPassword=valid_stringInput("Enter new Password = ")
        studentPassword=newPassword
    else:
        studentPassword="Abc123"
    student_name=valid_stringInput("Enter Student Full Name = ")
    father_name=valid_stringInput("Enter Student Father Name = ")
    age=valid_intInput("Enter Student age = ")
    gender=valid_charInput("Enter Student Gender (M/F) = ",['M','F'])
    dateofBirth=valid_dateInput("Enter Date of Birth (DD-MM-YYYY) = ",format="%d-%m-%Y")
    contact_no=valid_stringInput(("Enter Contant Number = "))
    email=valid_stringInput("Enter Student E-mail = ")
    address=valid_stringInput("Enter Student Address = ")
    admissionDate=valid_dateInput("Enter Admission Date (DD-MM-YYYY) = ",format="%d-%m-%Y")
    student_semester=valid_charInput("Enter Student Semester (1-8)= ",['1','2','3','4','5','6','7','8'])
    student_section=valid_charInput("Enter Student Section (A/B/C/D/E/F/G)= ",['A','B','C','D','E','F','G'])
    student_marks=valid_charInput("Do you want to enter student result (Y/N) = ",['Y','N'])
    if (student_marks=='Y'):
        s_Advance_Database,s_databaseGrade,s_Theory_of_Automata,s_toaGrade,s_Probability_and_Statistics,s_statGrade,s_Analysis_of_Algorithm,s_aoaGrade,s_Expository_Writing,s_expositoryGrade,s_Introduction_to_Management,s_managementGrade,s_totalMarks,s_percentage,s_cgpa=student_percentage()
    else:
        s_totalMarks=0
        s_percentage=0.0
        s_cgpa=0.0
        s_Advance_Database=s_Theory_of_Automata=s_Probability_and_Statistics=s_Analysis_of_Algorithm=s_Expository_Writing=s_Introduction_to_Management=0.0
        s_databaseGrade=s_toaGrade=s_statGrade=s_aoaGrade=s_expositoryGrade=s_managementGrade="N/A"

    with open("students.txt","a") as file:
        file.write(f"{str(student_id)},{studentPassword},{student_name},{father_name},{str(age)},{gender},{dateofBirth},{str(contact_no)},{email},{address},{admissionDate},{student_semester},{student_section},{str(s_totalMarks)},{str(s_percentage)},{str(s_cgpa)},{str(s_Advance_Database)},{s_databaseGrade},{str(s_Theory_of_Automata)},{s_toaGrade},{str(s_Probability_and_Statistics)},{s_statGrade},{str(s_Analysis_of_Algorithm)},{s_aoaGrade},{str(s_Expository_Writing)},{s_expositoryGrade},{str(s_Introduction_to_Management)},{s_managementGrade}\n")
    print("Student added Successfully\n")
    returnBackAdmin()

#Duplicate Studend Find (Add Student)
def duplicateStudent(student_id):
    with open("students.txt","r") as file1:
        lines=file1.readlines()
        for line in lines:
                existingId=line.strip().split(",")[0].strip()
                if(existingId==str(student_id)):
                    return True
    return False

#Student Percentage (Add Student)
def student_percentage():
    def valid_marks(subject):
        while True:
            marks=valid_floatInput(f"Enter {subject} marks between 0-100 = ")
            if marks>=0 and marks<=100:
                return marks
            else:
                print("\nPlease enter marks between 0-100\n")
    def get_grade(marks):
        if marks >= 90:
            return "A+"
        elif marks >= 80:
            return "A"
        elif marks >= 70:
            return "B"
        elif marks >= 60:
            return "C"
        elif marks >= 50:
            return "D"
        else:
            return "F"
    Advance_Database=valid_marks("Advance Database")
    databaseGrade=get_grade(Advance_Database)
    Theory_of_Automata=valid_marks("Theory of Automata")
    toaGrade=get_grade(Theory_of_Automata)
    Probability_and_Statistics=valid_marks("Probability & Statistics")
    statGrade=get_grade(Probability_and_Statistics)
    Analysis_of_Algorithm=valid_marks("Analysis of Algorithm")
    aoaGrade=get_grade(Analysis_of_Algorithm)
    Expository_Writing=valid_marks("Expository Writing")
    expositoryGrade=get_grade(Expository_Writing)
    Introduction_to_Management=valid_marks("Introduction to Management")
    managementGrade=get_grade(Introduction_to_Management)
    total=(Advance_Database+Theory_of_Automata+Probability_and_Statistics+Analysis_of_Algorithm+Expository_Writing+Introduction_to_Management)
    percentage=round((total/600)*100,2)
    cgpa=round((percentage/25),2)
    return Advance_Database,databaseGrade,Theory_of_Automata,toaGrade,Probability_and_Statistics,statGrade,Analysis_of_Algorithm,aoaGrade,Expository_Writing,expositoryGrade,Introduction_to_Management,managementGrade,total,percentage,cgpa

#Update Student (Admin Dashboard)
def updateStudent():
    clearscreen()
    with open("students.txt","r") as updatefile:
        studentRecords=updatefile.readlines()
        if not studentRecords:
            print("No Records found for update\n")
            returnBackAdmin()
        id=valid_intInput("Enter student Id for update = ")
        found=False
        for line in studentRecords:
            studentRecordData=line.strip().split(',')
            if (studentRecordData[0]==str(id)):
                print("1.Update Password\n2.Update Student Name\n3.Update Father Name\n4.Update Age\n5.Update Gender\n6.Update Date of Birth\n7.Update Contact Number\n8.Update E-mail\n9.Update Address\n10.Update Admission Date\n11.Update Semester\n12.Update Section\n13.Update Result\n14.Back to Admin Panel\n")
                updateChoice=valid_intInput("Enter your choice = ")
                match updateChoice:
                    case 1:
                        newStudentPassword=valid_stringInput("Enter new Id password = ")
                        studentRecordData[1]=newStudentPassword
                    case 2:
                        newstudent_name=valid_stringInput("Enter new Name = ")
                        studentRecordData[2]=newstudent_name
                    case 3:
                        newfather_name=valid_stringInput("Enter new Father Name = ")
                        studentRecordData[3]=newfather_name
                    case 4:
                        newage=valid_intInput("Enter new age = ")
                        studentRecordData[4]=str(newage)
                    case 5:
                        newgender=valid_charInput("Enter Gender (M/F) = ",['M','F'])
                        studentRecordData[5]=newgender
                    case 6:
                        newdateofBirth=valid_dateInput("Enter new Date of Birth (DD-MM-YYYY) = ")
                        studentRecordData[6]=newdateofBirth
                    case 7:
                        newcontact_no=valid_stringInput(("Enter new Contant Number = "))
                        studentRecordData[7]=newcontact_no
                    case 8:
                        newemail=valid_stringInput("Enter new E-mail = ")
                        studentRecordData[8]=newemail
                    case 9:
                        newaddress=valid_stringInput("Enter new Address = ")
                        studentRecordData[9]=newaddress
                    case 10:
                        newadmissionDate=valid_dateInput("Enter new Admission Date (DD-MM-YY) = ")
                        studentRecordData[10]=newadmissionDate
                    case 11:
                        newstudent_semester=valid_intInput("Enter new Student Semester = ")
                        studentRecordData[11]=str(newstudent_semester)
                    case 12:
                        student_section=valid_charInput("Enter Student new Section (A/B/C/D/E/F/G)= ",['A','B','C','D','E','F','G'])
                        studentRecordData[12]=student_section
                    case 13:       
                        newstudent_marks=valid_charInput("Do you want to enter new result (Y/N) = ",['Y','N'])       
                        if (newstudent_marks=='Y'):
                            s_Advance_Database,s_databaseGrade,s_Theory_of_Automata,s_toaGrade,s_Probability_and_Statistics,s_statGrade,s_Analysis_of_Algorithm,s_aoaGrade,s_Expository_Writing,s_expositoryGrade,s_Introduction_to_Management,s_managementGrade,s_total,s_percentage,s_cgpa=student_percentage()
                            studentRecordData[13:28]=[str(s_totalMarks),str(s_percentage),str(s_cgpa),str(s_Advance_Database),s_databaseGrade,str(s_Theory_of_Automata),s_toaGrade,str(s_Probability_and_Statistics),s_statGrade,str(s_Analysis_of_Algorithm),s_aoaGrade,str(s_Expository_Writing),s_expositoryGrade,str(s_Introduction_to_Management),s_managementGrade]
                        else:
                            s_totalMarks,s_percentage,s_cgpa,s_Advance_Database,s_databaseGrade,s_Theory_of_Automata,s_toaGrade,s_Probability_and_Statistics,s_statGrade,s_Analysis_of_Algorithm,s_aoaGrade,s_Expository_Writing,s_expositoryGrade,s_Introduction_to_Management,s_managementGrade=studentRecordData[13:28]
                    case 14:
                        adminPanel()
                    case _:
                        invalidOption()

                studentRecords[studentRecords.index(line)] = ",".join(studentRecordData) + "\n"
                with open("students.txt","w") as updatefile:
                    updatefile.writelines(studentRecords)
                    print("Record updated successfully!\n")
                returnBackAdmin()
                found=True
                break
        if not found:
                print("No record for this Id\n")
                returnBackAdmin()

#Delete Student(Admin Dashboard)
def deleteStudent():
    clearscreen()
    with open("students.txt","r") as deletefile:
        studentRecords=deletefile.readlines()
        if not studentRecords:
            print("No Records found for update\n")
            returnBackAdmin()
        id=valid_intInput("Enter student Id for deletion = ")
        found=False
        updateRecord=[]
        for line in studentRecords:
            studentRecordData=line.strip().split(',')
            if (studentRecordData[0]==str(id)):
                print(f"Record of {id} deleted successfully")
                found=True
                continue
            updateRecord.append(line)    
        if not found:
            print("No record for this id\n")
        else:
            with open("students.txt","w") as file:
                file.writelines(updateRecord)
        returnBackAdmin()

#Search Student(Admin Panel)
def searchStudent():
    clearscreen()
    with open("students.txt","r") as viewfile:
        studentRecords=viewfile.readlines()
        if not studentRecords:
            print("No Records found\n")
            returnBackAdmin()
        id=valid_intInput("Enter student Id for search = ")
        found=False
        for line in studentRecords:
            studentRecordData=line.strip().split(',')
            if (studentRecordData[0]==str(id)):
                print(f"\t--------Record of {studentRecordData[2]}--------")
                print(f"ID :{studentRecordData[0]}")
                print(f"Id Password : {studentRecordData[1]}")
                print(f"Name : {studentRecordData[2]}")
                print(f"Father Name : {studentRecordData[3]}")
                print(f"Age : {studentRecordData[4]}")
                print(f"Gender : {studentRecordData[5]}")
                print(f"DOB : {studentRecordData[6]}")
                print(f"Contact No : {studentRecordData[7]}")
                print(f"E-mail : {studentRecordData[8]}")
                print(f"Address : {studentRecordData[9]}")
                print(f"Admission Date : {studentRecordData[10]}")
                print(f"Semester : {studentRecordData[11]}")
                print(f"Section : {studentRecordData[12]}")
                print(f"Total Marks : {studentRecordData[13]}")
                print(f"Percentage : {studentRecordData[14]}%")
                print(f"CGPA : {studentRecordData[15]}")
                print(f"Advance Database : {studentRecordData[16]},{studentRecordData[17]}")
                print(f"Theory of Automata : {studentRecordData[18]},{studentRecordData[19]}")
                print(f"Probability and Statistics : {studentRecordData[20]},{studentRecordData[21]}")
                print(f"Analysis of Algorithm : {studentRecordData[22]},{studentRecordData[23]}")
                print(f"Expository Writing : {studentRecordData[24]},{studentRecordData[25]}")
                print(f"Introduction to Management : {studentRecordData[26]},{studentRecordData[27]}\n")
                found=True
                returnBackAdmin()
                break
        if not found:
                print("No record for this Id\n")
                returnBackAdmin()


#Filter Students
def filterStudent():
      clearscreen()
      print("1.Filter by Gender\n2.Filter by Semester\n3.Filter by Section\n4.Back to Admin Dashboard")
      filterChoice=valid_intInput("Enter your choice = ")
      match filterChoice:
            case 1:
              filterbyGender()  
            case 2:
              filterbySemester()
            case 3:
              filterbySection()
            case 4:
              returnBackAdmin()
            case __:
              invalidOption()

#Filter by Gender (Filter Students)             
def filterbyGender():
      clearscreen()
      filtergender=valid_charInput("Enter Student Gender (M/F) = ",['M','F'])
      with open("students.txt","r") as filterfile:
        studentRecords=filterfile.readlines()
        if not studentRecords:
            print("No Records found\n")
            returnBackAdmin()
        total=0
        for line in studentRecords:
            studentRecordData=line.strip().split(',')
            if (studentRecordData[5]==str(filtergender)):
                total+=1
        print(f"Total Records found for {filtergender} = {total}\n")
        returnBackfilter()
    
            
#Filter by Semester (Filter Students)
def filterbySemester():
      clearscreen()
      filterstudent_semester=valid_charInput("Enter Student Semester (1-8)= ",['1','2','3','4','5','6','7','8'])
      with open("students.txt","r") as filterfile:
        studentRecords=filterfile.readlines()
        if not studentRecords:
            print("No Records found\n")
            returnBackAdmin()
        total=0
        for line in studentRecords:
            studentRecordData=line.strip().split(',')
            if (studentRecordData[11]==str(filterstudent_semester)):
                total+=1
        print(f"Total Records found for semester {filterstudent_semester} = {total}\n")
        returnBackfilter()

#Filter by Section (Filter Students)
def filterbySection():
    clearscreen()
    filterstudent_section=valid_charInput("Enter Student Section (A/B/C/D/E/F/G)= ",['A','B','C','D','E','F','G'])
    with open("students.txt","r") as filterfile:
        studentRecords=filterfile.readlines()
        if not studentRecords:
            print("No Records found\n")
            returnBackAdmin()
        total=0
        for line in studentRecords:
            studentRecordData=line.strip().split(',')
            if (studentRecordData[12]==str(filterstudent_section)):
                total+=1
        print(f"Total Records found for section {filterstudent_section} = {total}\n")
        returnBackfilter()           

#Reset Records (Admin Dashboard)
def resetRecords():
    clearscreen()
    resetOption=valid_charInput("Are you sure to delete all records? (Y/N) = ",['Y','N'])
    if resetOption=='Y':
        with open("students.txt","w") as file:
            pass
            print("All records deleted successfully\n")
    elif resetOption=='N':
        print("Reset cancelled\n")
    returnBackAdmin()

#Change Password(Admin Dashboard)
def changePassword():
    clearscreen()
    old=valid_stringInput("Enter your old password = ")
    with open("adminCredentials.txt","r") as file:
        adminData=file.read().split(',')
    if(old!=adminData[1]):
        print("Incorrect Password\n")
        returnBackAdmin()
    newPassword=valid_stringInput("Enter new password = ")
    repeatPassword=valid_stringInput("Re-enter new password = ")
    if(newPassword!=repeatPassword):
        print("Password cannot reset\n")
        returnBackAdmin()
        return
    
    adminData[1]=newPassword
    with open("adminCredentials.txt","w") as file1:
        file1.write(",".join(adminData))
    print("Password updated Successfully\n")
    returnBackAdmin()
     
#Logout(Admin Dashboard)
def logOut():
    clearscreen()
    print("Logging out--------")
    time.sleep(1)
    clearscreen()
    mainMenu()
    
#Wrong Credentials (Admin Panel)
def wrongCredentials():
            clearscreen()
            print("Wrong credentials,Try Again")
            time.sleep(1)
            clearscreen()
            mainMenu()

#Valid Input
#Integer Input(Valid Input)
def valid_intInput(prompt):
    while True:
            value=input(prompt)
            if value=="":
                print("Input cannot be empty.Please enter a valid number")
                continue
            try:
                return int(value)
            except ValueError:
                print("Invalid Input,Please enter a valid number")

#Float Input(Valid Input)
def valid_floatInput(prompt1):
    while True:
            value1=input(prompt1).strip()
            if value1=="":
                print("Input cannot be empty.Please enter a valid number")
                continue
            try:
                return float(value1)
            except ValueError:
                print("Invalid Input,Please enter a valid number ")

#Char Input(Valid Input)
def valid_charInput(prompt2,validOptions=None):
    while True:
        character=input(prompt2).strip().upper()
        if character=="":
                print("Input cannot be empty.Please enter a valid character")
                continue
        char=character[0]
        if validOptions:
            if char in validOptions:
                return char
            else:
                print(f"Please enter a valid option {'/'.join(validOptions)}")

#String Input(Valid Input)
def valid_stringInput(prompt3):
    while True:
        string=input(prompt3).strip()
        if string=="":
            print("Input cannot be empty. Please enter valid string.")
        else:
            return string


#Date Input(Valid Input)
def valid_dateInput(prompt3,format="%d-%m-%Y"):
    while True:
        date=input(prompt3).strip()
        if date=="":
            print("Date cannot be empty.")
            continue
        try:
            validDate=datetime.strptime(date,format)
            return validDate
        except ValueError:
             print(f"Please enter a date in this format (DD-MM-YYYY) ")

#Return Back (Admin Dashboard)
def returnBackAdmin():
    input("Press any Key to return back to Admin Dashboard")
    admindashboard()

#Return View (View Menu)  
def returnBackView():
    input("Press any Key to return back to View Menu")
    viewStudent()

#Return Filter (Filter Menu)
def returnBackfilter():
    clearscreen()
    input("Press any Key to return back to Filter Menu")
    filterStudent()

#Clear Screen
def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')

#Student Panel
def studentPanel():
        clearscreen()
        print("\t--------Welcome to Student Panel--------")
        with open("students.txt","r") as viewfile:
            studentRecords=viewfile.readlines()
        if not studentRecords:
            print("Portal is under progress")
            time.sleep(1)
            mainMenu()
        id=valid_intInput("Enter your Student ID = ")
        password=valid_stringInput("Enter your Password = ")
        found=False
        for line in studentRecords:
            studentRecordData=line.strip().split(',')
            if(studentRecordData[0]==str(id) and studentRecordData[1]==password):
                found=True
                studentdashboard(studentRecordData)
        if not found:
                print("No record for this Id and password")
                wrongCredentials()

#Student Dashboard      
def studentdashboard(data):
    clearscreen()
    while True:
        print("\t--------Welcome to Student Dashboard--------")
        print("1.View Profile \n2.View Result \n3.View Classmate\n4.Change Password\n5.Logout")
        studentChoice=valid_intInput("Enter your choice = ")
        match studentChoice:
            case 1:
                viewProfile(data)
                break
            case 2:
                viewResult(data)
                break
            case 3:
                viewClassmates(data)
                break
            case 4:
                studentchangePassword(data)
                break
            case 5:
                logOut()
                break
            case _:
                invalidOption()

#View Profile (Student Dashboard)
def viewProfile(data):
        clearscreen()
        print(f"\t--------Welcome {data[2]}--------\n")
        print(f"Roll No : {data[0]}")     
        print(f"Your Name : {data[2]}")
        print(f"Your Father Name : {data[3]}")
        print(f"Your Age : {data[4]}")
        print(f"Your Gender : {data[5]}")
        print(f"Your DOB : {data[6]}")
        print(f"Your Contact No : {data[7]}")
        print(f"Your E-mail : {data[8]}")
        print(f"Your Address : {data[9]}")
        print(f"Your Admission Date : {data[10]}")
        print(f"Your Semester : {data[11]}")
        print(f"Your Section : {data[12]}")
        print(f"Your CGPA : {data[15]}\n")
        returnBackStudent(data)
   
#View Result (Student Dasboard)
def viewResult(data):
    clearscreen()
    print("\t--------Your Result--------\n")
    print(f"Name : {data[2]} \nRoll No : {data[0]}\nSemester : {data[11]}-{data[12]}\n\n")
    print(f"Subjects: \n1.Advance Database = {data[16]}\nGrade = {data[17]}\n2.Theory of Automata = {data[18]}\nGrade = {data[19]}\n3.Probability and Statistics = {data[20]}\nGrade = {data[21]}\n4.Analysis of Algorithm = {data[22]}\nGrade = {data[23]}\n5.Expository Writing = {data[24]}\nGrade = {data[25]}\n6.Introduction to Management = {data[26]}\nGrade = {data[27]}\n")
    print(f"Total Marks = {data[13]}\nPercentage = {data[14]}%\nCGPA = {data[15]}")
    returnBackStudent(data)

#View Classmates (Student Dashboard)
def viewClassmates(data):
    clearscreen()
    with open("students.txt","r") as viewfile:
        studentRecords=viewfile.readlines()
        studentRecords.sort(key=lambda records: records.split(',')[0])
        total=total1=total2=0
        print(f"\t\t-------------Record of {data[11]}-{data[12]}-------------\n")
        for line in studentRecords:
            studentRecordData=line.strip().split(',')
            print("\t\tRoll NO\t\t:\t\tName     ")
            if (studentRecordData[11]==data[11] and studentRecordData[12]==data[12] ):
                total+=1
                if (studentRecordData[5]=='M'):
                    total1+=1
                elif (studentRecordData[5]=='F'):
                    total2+=1
                print(f"\t\t{studentRecordData[0]}\t\t:\t\t{studentRecordData[2]}\n")
                     
    print(f"Total Students in {data[11]}-{data[12]} = {total}")
    print(f"Total Male Students in {data[11]}-{data[12]} = {total1}")
    print(f"Total Female Students in {data[11]}-{data[12]} = {total2}\n")
    returnBackStudent(data)

#Student Change Password(Student Dashboard)
def studentchangePassword(data):
    clearscreen()
    old=valid_stringInput("Enter your old password = ")
    if(old!=data[1]):
        print("Incorrect Password\n")
        returnBackStudent(data)
    newPassword=valid_stringInput("Enter new password = ")
    repeatPassword=valid_stringInput("Re-enter new password = ")
    if(newPassword!=repeatPassword):
        print("Password cannot reset\n")
        returnBackStudent(data)
        return
    
    data[1]=newPassword
    with open("students.txt","w") as file1:
        file1.write(",".join(data))
    print("Password updated Successfully\n")
    returnBackStudent(data)
    
#Return Back (Student Dashboard)
def returnBackStudent(data):
    input("Press any Key to return back to Student Dashboard")
    studentdashboard(data)

#Exit (Main menu)
def Exit():
    clearscreen()
    print("Exiting---------")
    time.sleep(1)
    clearscreen()
    exit()

#Invalid Option
def invalidOption():
    clearscreen()
    print("Invalid Option! Please Enter correct option")
    time.sleep(2)
    clearscreen()

mainMenu()



print("..........Admmission Eligibility Check..........")
age=int(input("Enter Age Of Student:"))
marks=int(input("Enter Marks:"))

if(age>=17 and age<=25):
    print("Eligible for Admission by Age")

    if(marks>60):
        print("Eligible for B.Tech")

        if(marks>85):
            print("Eligible for AIML")
        
        elif(marks>75):
            print("Eligible For CSE")
        
        else:
            print("Eligible for MECH,ENTC,CIVIL,ELECTRICAL")
    
    else:
        print("Not Eligible for B.Tech")

else:
    print("Not Eligible for Admission by Age")

print("........🙏🙏Thank you🙏🙏..........")

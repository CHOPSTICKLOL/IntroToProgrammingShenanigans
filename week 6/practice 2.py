cls=int(input("Write the number of classes held:"))
atd=int(input("Write the number of classes you attended:"))
cause=input("Do you have a cause(y or n):")
percentage=atd/cls*100
if percentage>=70:
   print("You are allowed to take the exam")
else:
    if cause=="y":
        print("since you have a medical cause ill let you live")
    else:
        print("get out bigot")



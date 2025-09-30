number= 8
guess= int(input("yout guess:"))
counter=0
while guess != number:
    guess= int(input("try again???"))
    counter+=1
if counter <2:
    print("jarvis, clean my pants")
elif counter <5:
    print("jarvis, i edged")
else:
    print("kill this korean whore")
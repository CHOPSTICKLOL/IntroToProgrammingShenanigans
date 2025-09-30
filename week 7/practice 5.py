num=int(input("how many integers u want in list"))
lst=[]
c=0
for x in range (num):
    item=(int(input(f"pls tell me the num{x+1}")))
    lst.append(item)
    if item%2==0:
        c+=1
print(f"you have {c} even numbers in the list")




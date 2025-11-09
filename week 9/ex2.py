lst=[]
counter=1
while len(lst)<5:
    num=int(input(f"enter a number{counter}: "))
    lst.append(num)
    counter+=1
    print(lst)
for x in range(len(lst)):
    if lst[x]>10:
        print(f"number={lst[x]}, index={x}") #the x is the index of the elements always

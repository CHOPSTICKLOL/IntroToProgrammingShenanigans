lst=[]
counter=1
while len(lst)<5:
    num=int(input(f"pls add numero{counter}:"))
    counter+=1
    lst.append(num)
for x in range(len(lst)):
    if lst[x]>10:
        print(f"{lst[x]} in {x}")

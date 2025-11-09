lst =[]
pplnum=int(input("how many people do you want in the event?:"))
counter = 1
while len(lst)<pplnum:#always remember to use length of the list
    ppl=input(f"please add the person number {counter}:")
    counter+=1
    lst.append(ppl)
    print(lst)
for x in range(len(lst)):
    if lst[x][0]=="a":
        print(lst[x])
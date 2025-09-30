num=int(input("how many games did u buy?"))
lst=[]
for x in range (num):
    item=(int(input(f"pls tell me the price{x+1}:")))
    lst.append(item)
print(lst)
totalgem=sum(lst)
print(f"you have spent {totalgem}$ for games")
if totalgem>100:
    print("you've spent too much")

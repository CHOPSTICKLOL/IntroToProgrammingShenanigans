num=int(input("how msny things do u wanna buy?:"))
lst=[]
for x in range (num):
    item=(input(f"pls tell me the item num{x+1}"))
    lst.append(item)
    print("your items are:")
print(lst)

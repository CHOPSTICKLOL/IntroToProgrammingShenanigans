list=["1","2","3","4","5"]
print(list[0],list[2],list[4])
print(list[-5],list[-3],list[-1])
list[2]=42
new=input("pls add new value")
num=int(new)
list.append(num)
print(list)
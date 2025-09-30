lst=[1,3,7,4,5]
cnt=[]
for i in range(len(lst)):
    if i%2 !=0:
        cnt.append(int(lst[i]*2))
    else:
        cnt.append(int(lst[i] * 3))
print(cnt)
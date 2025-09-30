a=[int(input("pls add integer"))for i in range(4)]
max=a[0]
for i in a:
    if i>max:
        max=i
print(max)
list=[int(input("Enter your ints")) for i in range(4)]
print(list)
max= list[0]
for element in list:
    if element > max:
        max=element
print(max)

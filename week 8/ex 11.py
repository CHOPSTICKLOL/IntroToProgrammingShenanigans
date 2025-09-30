my_list=[1,2,3]
total= 0
for number in my_list:
    total+=number
while total/len(my_list)<=5:
    new=int(input("new num pls:"))
    my_list.append(new)
    total+=new
print(f"the new list is {my_list}, and the avg is {total/len(my_list)}")
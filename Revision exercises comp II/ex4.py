def reverse_list(lst):
    reversed_list=[]
    for i in range(len(lst)-1,-1,-1):
        reversed_list.append(lst[i])
    return reversed_list
nigga=[1,2,3,4,5,6,6,7]
print(reverse_list(nigga))
#since the step value is -1 it goes backwards
def split_list(lst):
    left=lst[0:len(lst)//2]
    right=lst[len(lst)//2:]
    return left,right
shaahir=[1,2,4,5,6,77,32]
left1,right1 =split_list(shaahir)
print("l1=",left1,"r2=",right1)



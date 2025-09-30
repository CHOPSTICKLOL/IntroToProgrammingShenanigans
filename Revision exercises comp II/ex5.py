def is_even(gg):
    if gg%2==0:
        return True
    else:
        return False
def count_even(ff):
    lst=[]
    for number in ff:
        if number%2==0:
            lst.append(number)
    return len(lst)
chigga=9
print(is_even(chigga))
nigga=[1,2,3,4,8]
print(count_even(nigga))

def find_minimum(lst):
    mex=lst[0]
    for numbers in lst:
        if numbers<mex:
            mex=numbers
    return mex
leander=[1,2,3,-84,5,1,6,-56]
print(find_minimum(leander))







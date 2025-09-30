def ordered_pass(lst):
    for i in range(len(lst) - 1):

        if lst[i]>lst[i+1]:
            lst[i],lst[i+1]=lst[i+1],lst[i]
    return lst
nums = [5, 1, 4, 2, 8]
print(ordered_pass(nums))








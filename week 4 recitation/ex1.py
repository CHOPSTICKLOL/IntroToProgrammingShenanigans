def find_zero_sum_pairs_naive(lst):
    new=[]
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i]+lst[j]==0:
                new.append((lst[i], lst[j]))
    return new
q=[11,22,-33,44,-44,-11]
print(find_zero_sum_pairs_naive(q))




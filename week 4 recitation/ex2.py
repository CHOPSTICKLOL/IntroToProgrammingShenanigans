def find_zero_sum_pairs_optimized(lst):
    count_dict = {}
    pairs=set()

    for num in lst:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    print(count_dict)
    for num in count_dict:
        if -num in count_dict:
            pair=tuple(sorted((num, -num)))
            pairs.add(pair)
    return list(pairs)
e=[1,2,2,3,4,5,-2,-2,-5]
print(find_zero_sum_pairs_optimized(e))



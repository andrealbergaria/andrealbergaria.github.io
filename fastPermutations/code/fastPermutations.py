def permutation(lst):
    l = lst
    result_list = []

    for i in range(0,len(lst)):
        l = l[1:] + l[:1]
        result_list.append(l)
    input(f" {result_list}")
    return result_list

#Driver code
permutation([1,2,34,4,5,67,78])

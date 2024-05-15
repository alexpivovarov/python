def insertion_sort(list_a):
    indexing_length = range(1, len(list_a)) # we start at the position 1 because item at position 0 is already sorted
    for i in indexing_length:
        value_to_sort = list_a[i]

        while list_a[i-1] > value_to_sort and i > 0:
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
            i = i -1

    return list_a

print(insertion_sort([2,0,1,6,9,8]))

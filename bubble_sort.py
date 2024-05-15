def bubble(unsorted_list):
    indexing_length = len(unsorted_list) - 1 # -1 because we cannot perform a comparison on the last number of the list as there is no number after it
    sorted = False # this is our flag

    while not sorted: # = as long as variable "sorted" is False
        sorted = True
        for i in range(0, indexing_length):
            if unsorted_list[i] > unsorted_list[i+1]:
                sorted = False
                unsorted_list[i], unsorted_list[i+1] = unsorted_list[i+1], unsorted_list[i]
    return unsorted_list

print(bubble([2, 0, 4, 9, 1, 1]))

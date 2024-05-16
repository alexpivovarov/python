def selection_sort(arr):
    for i in range(0, len(arr) - 1):  # the last index can be skipped because when algorithm arrives at this point the last element is in the correct position
        cur_min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[cur_min_index]:
                cur_min_index = j

        arr[i], arr[cur_min_index] = arr[cur_min_index], arr[i]  # swap


arr = [0, 2, 6, 8, 2, 1]
selection_sort(arr)
print(arr)

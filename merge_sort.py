def merge_sort(arr):
    if len(arr) > 1:  # if length is not greater than 1 array is already sorted 
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]
        
        # recursion step
        merge_sort(left_arr)
        merge_sort(right_arr)
 
        # merge step
        i = 0 # left array index
        j = 0 # right array index
        k = 0 # merged array idx 
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else: 
                arr[k] = right_arr[j]
                j += 1
            k += 1
            
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
            
        while j < len(right_arr) :
            arr[k] = right_arr[j]
            j += 1
            k += 1
                
                
arr_test = [4, 2, 5, 7, 1, 0, 4, 6] 
merge_sort(arr_test)
print(arr_test)
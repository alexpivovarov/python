def binary_search(sequence, item):
    begin_index = 0
    end_index = len(sequence) - 1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = sequence[midpoint]
        if midpoint_value == item:
            return midpoint  # (returning position of midpoint)

        elif item < midpoint_value:
            end_index = midpoint - 1

        else:
            begin_index = midpoint + 1

    return None  # return none if the item is not found in the sequence (when while loop breaks)

sequence_1 = [0, 5, 6, 7, 7, 10, 14, 15, 21] # (list must be already ordered)
item_1 = 14

print(binary_search(sequence_1, item_1))
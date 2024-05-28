'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Examples:

Input : [0, 1, 0, 3, 12]
Output : [1, 3, 12, 0, 0]

Note:
    1. You must do this in-place without making a copy of the array.
    2. Minimise the total number of operations

'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        prev_idx = 0 # keeps track of the position where the next non-zero element should be placed.
        for i in range(0, len(nums)): # iterate through the array using a for loop
            if nums[i] != 0: # checking if the current element nums[i] is not zero
                hold = nums[prev_idx] # temporarily hold the value at nums[prev_idx]
                nums[prev_idx] = nums[i] # set nums[prev_idx] to nums[i]
                nums[i] = hold # set nums[i] to the held value.
                prev_idx += 1 # incrementing prev_index
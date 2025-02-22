from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0
        curr_sum = nums[0]  # Start with the first element
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:  # Continue ascending sequence
                curr_sum += nums[i]
            else:  # Reset when sequence breaks
                max_sum = max(max_sum, curr_sum)
                curr_sum = nums[i]  # Start a new sequence
                
        return max(max_sum, curr_sum)  # Return the max found

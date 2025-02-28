from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        
        # Initialize with the first element.
        current_max = nums[0]
        max_sum = nums[0]
        current_min = nums[0]
…        # Maximum absolute sum is the maximum between max_sum and the absolute of min_sum.
        result = max(max_sum, abs(min_sum))
        
        # Since empty subarray (with sum 0) is allowed, result is at least 0.
        result = max(result, 0)
        return result % mod

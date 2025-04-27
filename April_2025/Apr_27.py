from typing import List

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        for i in range(n - 2):
            a = nums[i]
            b = nums[i + 1]
            c = nums[i + 2]
            if 2 * (a + c) == b:
                count += 1
        return count

from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for mask in range(1 << n):
            current_xor = 0
            for i in range(n):
                if mask & (1 << i):
                    current_xor ^= nums[i]
            total += current_xor
        return total

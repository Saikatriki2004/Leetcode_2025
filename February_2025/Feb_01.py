from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):  # Iterate over adjacent pairs
            if (nums[i] % 2) == (nums[i + 1] % 2):  # Same parity check
                return False
        return True

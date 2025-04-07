from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True  # Base case: sum 0 is achievable
        
        for num in nums:
            # Iterate backwards to avoid using the same element multiple times
            for j in range(target, num - 1, -1):
                if dp[j - num]:
                    dp[j] = True
            if dp[target]:
                return True
        
        return dp[target]

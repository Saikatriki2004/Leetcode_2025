from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums.sort()
        n = len(nums)
        dp = [1] * n  # dp[i] stores the length of the largest subset ending with nums[i]
        parent = [-1] * n  # parent[i] stores the index of the previous element in the subset
        
        max_length = 1
        max_index = 0
        
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        parent[i] = j
            # Update the maximum length and corresponding index
            if dp[i] > max_length:
                max_length = dp[i]
                max_index = i
        
        # Reconstruct the subset
        result = []
        current = max_index
        while current != -1:
            result.append(nums[current])
            current = parent[current]
        
        return result[::-1]

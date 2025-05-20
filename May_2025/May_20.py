from typing import List

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        # 1) Build a difference array for coverage counts:
        diff = [0] * (n + 1)
        for l, r in queries:
            diff[l]   += 1
            diff[r+1] -= 1   # safe since diff has length n+1

        # 2) Prefix‐sum to get coverage count at each index
        cover = [0] * n
        cur = 0
        for i in range(n):
            cur       += diff[i]
            cover[i]   = cur

        # 3) Check feasibility: each index i must be covered at least nums[i] times
        for i, need in enumerate(nums):
            if cover[i] < need:
                return False

        return True

from typing import List

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        
        def can_make(threshold: int) -> bool:
            count = i = 0
            n = len(nums)
            while i + 1 < n and count < p:
                if nums[i+1] - nums[i] <= threshold:
                    count += 1
                    i += 2
                else:
                    i += 1
            return count >= p

        lo, hi = 0, nums[-1] - nums[0]
        while lo < hi:
            mid = (lo + hi) // 2
            if can_make(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo

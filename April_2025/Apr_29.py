from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        positions = [i for i, num in enumerate(nums) if num == max_val]
        m = len(positions)
        if m < k:
            return 0
        
        res = 0
        n = len(nums)
        
        for j in range(k - 1, m):
            i = j - k + 1
            prev_pos = positions[i - 1] if i > 0 else -1
            start_choices = positions[i] - prev_pos
            end_choices = n - positions[j]
            res += start_choices * end_choices
        
        return res

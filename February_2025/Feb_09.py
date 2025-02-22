from typing import List
from collections import defaultdict

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        # Total pairs (i, j) with i < j
        total_pairs = n * (n - 1) // 2
        
        # Dictionary to count frequency of d = i - nums[i]
        freq = defaultdict(int)
        for i, x in enumerate(nums):
            key = i - x
            freq[key] += 1
        
        # Count the number of good pairs
        good_pairs = 0
        for count in freq.values():
            good_pairs += count * (count - 1) // 2
        
        # Bad pairs are total pairs minus good pairs
        return total_pairs - good_pairs

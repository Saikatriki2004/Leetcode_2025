from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        count_even = 1  # There is one even prefix initially (sum = 0)
        count_odd = 0
        prefix = 0
        res = 0
        
        for x in arr:
            # Only the parity matters, so we add x mod 2.
            prefix = (prefix + (x % 2)) % 2
            
            if prefix == 0:
                # Current prefix is even, so to get odd sum subarray,
                # the earlier prefix must be odd.
                res += count_odd
                count_even += 1
            else:
                # Current prefix is odd, so to get an odd subarray sum,
                # the earlier prefix must be even.
                res += count_even
                count_odd += 1
                
            res %= MOD
        
        return res

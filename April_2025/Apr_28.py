from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        res = 0
        
        for i in range(n):
            low = i
            high = n - 1
            best_j = i - 1  # Initialize to a value indicating no valid subarray
            
            while low <= high:
                mid = (low + high) // 2
                current_sum = prefix[mid + 1] - prefix[i]
                current_length = mid - i + 1
                product = current_sum * current_length
                
                if product < k:
                    best_j = mid
                    low = mid + 1
                else:
                    high = mid - 1
            
            if best_j >= i:
                res += best_j - i + 1
        
        return res

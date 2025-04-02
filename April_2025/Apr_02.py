from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        
        # Step 1: Precompute max_so_far for each j (max of nums[0..j-1])
        max_so_far = [0] * n
        for j in range(1, n):
            max_so_far[j] = max(max_so_far[j-1], nums[j-1])
        
        # Step 2: Compute val[j] = max_so_far[j] - nums[j]
        val = [0] * n
        for j in range(1, n):
            val[j] = max_so_far[j] - nums[j]
        
        # Step 3: Compute max_val_upto[j], the maximum val up to j
        current_max = -float('inf')
        max_val_upto = [-float('inf')] * n
        for j in range(1, n):
            current_max = max(current_max, val[j])
            max_val_upto[j] = current_max
        
        # Step 4: For each k >=2, compute the maximum product
        max_product = -float('inf')
        for k in range(2, n):
            current_max_val = max_val_upto[k-1]
            product = current_max_val * nums[k]
            if product > max_product:
                max_product = product
        
        return max(max_product, 0)

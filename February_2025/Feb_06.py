from collections import defaultdict
from typing import List

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_count = defaultdict(int)
        n = len(nums)
        
        # Count occurrences of each product
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                product_count[product] += 1

        # Calculate the number of valid tuples
        count = 0
        for freq in product_count.values():
            if freq > 1:
                count += (freq * (freq - 1) // 2) * 8  # 8 arrangements per pair
        
        return count

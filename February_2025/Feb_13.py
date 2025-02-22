import heapq
from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Convert the list into a min-heap.
        heapq.heapify(nums)
        operations = 0
        
        # Continue performing operations until the smallest element is at least k.
        while nums[0] < k:
            # There must be at least 2 elements to combine.
            if len(nums) < 2:
                break  # In theory this should not happen because answer is guaranteed.
            
            # Remove the two smallest numbers.
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            
            # Create a new number as per the operation.
            new_val = 2 * x + y
            
            # Push the new number back into the heap.
            heapq.heappush(nums, new_val)
            
            # Increment the operation count.
            operations += 1
        
        return operations

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Flatten the grid into a list
        nums = [a for row in grid for a in row]
        
        # Get the common remainder
        r = nums[0] % x
        
        # Check if all elements have the same remainder modulo x
        for num in nums:
            if num % x != r:
                return -1
        
        # Transform the elements to a' = (a - r) // x
        nums_prime = [(num - r) // x for num in nums]
        
        # Sort the transformed list
        sorted_nums = sorted(nums_prime)
        
        # Find the median (middle element after sorting)
        median = sorted_nums[len(sorted_nums) // 2]
        
        # Calculate total operations as sum of |a' - median|
        total_operations = sum(abs(a - median) for a in sorted_nums)
        
        return total_operations

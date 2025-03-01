class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Step 1: Apply the operations sequentially
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        # Step 2: Shift all zeros to the end
        # Collect non-zero elements while preserving their order
        non_zero = [num for num in nums if num != 0]
        
        # Create the result by appending zeros
        # Number of zeros = original length - number of non-zero elements
        result = non_zero + [0] * (n - len(non_zero))
        
        return result

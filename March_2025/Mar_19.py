class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        operation_count = 0
        prev2 = 0  # x_{i-2}
        prev1 = 0  # x_{i-1}
        
        # Process positions where operations can start
        for i in range(n - 2):
            b_i = 1 if nums[i] == 0 else 0  # Required flip parity
            if i == 0:
                x_i = b_i
            elif i == 1:
                x_i = b_i ^ prev1
            else:
                x_i = b_i ^ prev2 ^ prev1
            if x_i:
                operation_count += 1
            # Update previous values
            prev2 = prev1
            prev1 = x_i
        
        # Compute flip for j = n-2
        if n == 3:
            flip_n_minus_2 = prev1  # x_0
        else:
            flip_n_minus_2 = prev2 ^ prev1  # x_{n-4} ^ x_{n-3} for n >= 4
        
        # Required flip parities for last two positions
        b_n_minus_2 = 1 if nums[n - 2] == 0 else 0
        b_n_minus_1 = 1 if nums[n - 1] == 0 else 0
        
        # Verify if the solution is valid
        if flip_n_minus_2 == b_n_minus_2 and prev1 == b_n_minus_1:
            return operation_count
        return -1

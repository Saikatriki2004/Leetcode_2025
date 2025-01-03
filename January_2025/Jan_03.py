class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)  # Total sum of the array
        prefix_sum = 0  # To keep track of the sum of the first part
        valid_splits = 0
        
        for i in range(len(nums) - 1):  # Exclude the last index
            prefix_sum += nums[i]  # Update prefix sum
            suffix_sum = total_sum - prefix_sum  # Calculate suffix sum
            if prefix_sum >= suffix_sum:  # Check the condition
                valid_splits += 1
                
        return valid_splits

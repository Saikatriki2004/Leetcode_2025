class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # Initialize variables
        n = len(nums)
        if n == 1:
            return 1  # Single element array is trivially increasing or decreasing
        
        longest = 1  # At least one element is a subarray
        increasing = 1  # Length of the current increasing subarray
        decreasing = 1  # Length of the current decreasing subarray
        
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                increasing += 1  # Current element is greater, so increase the increasing subarray length
                decreasing = 1  # Reset the decreasing subarray length
            elif nums[i] < nums[i-1]:
                decreasing += 1  # Current element is smaller, so increase the decreasing subarray length
                increasing = 1  # Reset the increasing subarray length
            else:
                # If elements are equal, both increasing and decreasing subarrays are reset to 1
                increasing = 1
                decreasing = 1
            
            # Update the longest length found so far
            longest = max(longest, increasing, decreasing)
        
        return longest

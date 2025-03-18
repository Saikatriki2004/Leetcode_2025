class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        current_xor = 0
        max_length = 1
        
        for right in range(len(nums)):
            # Shrink window while there's a bit conflict
            while (nums[right] & current_xor) != 0:
                current_xor ^= nums[left]
                left += 1
            # Add the current element
            current_xor ^= nums[right]
            # Update the maximum length
            max_length = max(max_length, right - left + 1)
        
        return max_length

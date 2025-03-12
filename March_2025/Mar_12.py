class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # Helper function to find the rightmost index where nums[i] < 0
        def find_rightmost_negative():
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < 0:
                    left = mid + 1  # Look for a negative number further right
                else:
                    right = mid - 1  # Move left if mid is not negative
            return right  # Rightmost index where nums[i] < 0

        # Helper function to find the leftmost index where nums[i] > 0
        def find_leftmost_positive():
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] > 0:
                    right = mid - 1  # Look for a positive number further left
                else:
                    left = mid + 1  # Move right if mid is not positive
            return left  # Leftmost index where nums[i] > 0

        # Get the boundary indices
        rightmost_neg = find_rightmost_negative()
        leftmost_pos = find_leftmost_positive()

        # Calculate count of negative numbers
        neg_count = rightmost_neg + 1 if rightmost_neg >= 0 and nums[rightmost_neg] < 0 else 0
        
        # Calculate count of positive numbers
        pos_count = len(nums) - leftmost_pos if leftmost_pos < len(nums) and nums[leftmost_pos] > 0 else 0

        # Return the maximum of the two counts
        return max(neg_count, pos_count)

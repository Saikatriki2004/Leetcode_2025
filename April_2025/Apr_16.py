from collections import defaultdict

class Solution:
    def countGood(self, nums: list[int], k: int) -> int:
        n = len(nums)
        freq = defaultdict(int)
        total_pairs = 0
        left = 0
        result = 0
        
        for right in range(n):
            # Add the current element to the window
            x = nums[right]
            # The number of new pairs added by this element is equal to the current frequency of x
            total_pairs += freq[x]
            freq[x] += 1  # Increment the frequency of x
            
            # Shrink the window from the left as much as possible while the total_pairs >= k
            while total_pairs >= k:
                # Remove the leftmost element from the window
                y = nums[left]
                # The number of pairs removed is the frequency of y minus 1 (before decrementing)
                total_pairs -= (freq[y] - 1)
                freq[y] -= 1
                left += 1
            
            # The number of valid subarrays ending at 'right' is the current left index
            # because all subarrays starting from 0 to left-1 are valid
            result += left
        
        return result

from collections import defaultdict

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        # Initialize frequency map with prefix sum 0 having frequency 1
        freq = defaultdict(int)
        freq[0] = 1
        
        prefix_sum = 0
        answer = 0
        
        # Iterate through the array
        for num in nums:
            # Update prefix_sum: add 1 if num % modulo == k, else 0
            prefix_sum += (num % modulo == k)
            
            # Current prefix sum modulo modulo
            current_mod = prefix_sum % modulo
            
            # Target value needed for the subarray sum % modulo == k
            target = (current_mod - k) % modulo
            
            # Add the number of previous prefixes that make the subarray interesting
            answer += freq[target]
            
            # Update the frequency of the current prefix sum modulo
            freq[current_mod] += 1
        
        return answer

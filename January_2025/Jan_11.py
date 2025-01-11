class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # If k is greater than the length of the string, it's impossible
        if k > len(s):
            return False
        
        # Count frequency of each character
        from collections import Counter
        char_count = Counter(s)
        
        # Count the number of characters with odd frequency
        odd_count = sum(1 for count in char_count.values() if count % 2 != 0)
        
        # To form k palindromes, there must be at most k odd frequencies
        return odd_count <= k

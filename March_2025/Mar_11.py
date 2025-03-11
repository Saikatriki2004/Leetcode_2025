class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        # Calculate total number of substrings
        total = n * (n + 1) // 2
        
        # Initialize sliding window variables
        left = 0
        freq = {}  # Frequency dictionary for characters in the window
        distinct = 0  # Number of distinct characters in the window
        at_most_2 = 0  # Count of substrings with at most 2 distinct characters
        
        # Iterate over the string with the right pointer
        for right in range(n):
            char = s[right]
            # If the character’s frequency was 0, it’s a new distinct character
            if freq.get(char, 0) == 0:
                distinct += 1
            freq[char] = freq.get(char, 0) + 1
            
            # Shrink the window if distinct characters exceed 2
            while distinct > 2 and left <= right:
                remove_char = s[left]
                freq[remove_char] -= 1
                if freq[remove_char] == 0:
                    distinct -= 1
                left += 1
            
            # Add the number of valid substrings ending at right
            at_most_2 += right - left + 1
        
        # Number of substrings with exactly 3 distinct characters
        return total - at_most_2

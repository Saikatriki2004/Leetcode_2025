class Solution:
    def maxScore(self, s: str) -> int:
        # Count total ones in the string
        total_ones = s.count('1')
        
        # Initialize variables to track left zeros and the maximum score
        left_zeros = 0
        max_score = float('-inf')
        
        # Traverse the string and calculate the score for each split point
        # We iterate up to len(s) - 1 because both substrings must be non-empty
        for i in range(len(s) - 1):
            # Update the count of zeros and ones in the left substring
            if s[i] == '0':
                left_zeros += 1
            else:
                total_ones -= 1
            
            # Calculate the score for the current split
            score = left_zeros + total_ones
            
            # Update the maximum score
            max_score = max(max_score, score)
        
        return max_score

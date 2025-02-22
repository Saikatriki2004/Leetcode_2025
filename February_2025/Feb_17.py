from collections import Counter
from typing import List

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        freq = Counter(tiles)
        
        # backtrack returns the number of sequences starting from the current state.
        def backtrack() -> int:
            count = 0
            for ch in freq:
                if freq[ch] > 0:
                    # Use this letter: count the sequence formed by adding it
                    count += 1  
                    freq[ch] -= 1
                    count += backtrack()
                    freq[ch] += 1  # backtrack
            return count
        
        return backtrack()

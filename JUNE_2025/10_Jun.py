class Solution:
    def countStrings(self, s: str) -> int:
        n = len(s)
        # total number of ways to pick two different indices
        total_pairs = n * (n - 1) // 2
        
        # count how many index-pairs hold the same character
        from collections import Counter
        freq = Counter(s)
        duplicate_pairs = sum(f * (f - 1) // 2 for f in freq.values())
        
        if duplicate_pairs > 0:
            # swaps of identical chars give back the original string (count that once)
            return total_pairs - duplicate_pairs + 1
        else:
            # all swaps yield new strings
            return total_pairs

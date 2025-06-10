from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        
        # Collect odd and even frequencies
        odd_freqs  = [f for f in freq.values() if f % 2 == 1]
        even_freqs = [f for f in freq.values() if f % 2 == 0]
        
        # By problem statement, there's at least one odd and one even
        return max(odd_freqs) - min(even_freqs)

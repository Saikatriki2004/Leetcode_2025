class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # If already equal, return True
        if s1 == s2:
            return True
        
        # Find mismatched indices
        mismatches = [(a, b) for a, b in zip(s1, s2) if a != b]
        
        # Must have exactly 2 mismatches, and swapping should fix it
        return len(mismatches) == 2 and mismatches[0] == mismatches[1][::-1]

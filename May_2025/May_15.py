from typing import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        """
        Return a longest subsequence of `words` whose corresponding `groups` bits alternate.
        Greedy: at most one pick per contiguous block of identical bits.
        Time: O(n), Space: O(1) aside from output.
        """
        n = len(words)            if last_bit is None or g != last_bit:
                result.append(w)
                last_bit = g
        
        return result

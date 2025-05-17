from typing import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        """
        Return a longest subsequence of `words` whose corresponding `groups` bits alternate.
        Greedy: at most one pick per contiguous block of identical bits.
        Time: O(n), Space: O(1) aside from output.
        """
        n = len(words)
        if n == 0:
            return []
        
        result = []
        # last_bit is the bit of the last word we added to result
        # initialize to None so that the very first element always counts
        last_bit = None
        
        for w, g in zip(words, groups):
            # if it's the first pick, or this bit differs from last_bit, we can append
            if last_bit is None or g != last_bit:
                result.append(w)
                last_bit = g
        
        return result
from collections import Counter
from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        cnt = Counter()
        length = 0
        has_middle = False

        for w in words:
            rev = w[::-1]
            # If there's an unmatched reverse already in cnt, pair it up.
            if cnt[rev] > 0:
                cnt[rev] -= 1
                # Each pair of two-letter words adds 4 chars to the palindrome.
                length += 4
            else:
                # Otherwise, we hold this word for a future match.
                cnt[w] += 1

        # After pairing all non-palindromic pairs, handle the palindromes like "gg", "cc"
        # Any leftover single double-word can serve as the center of the palindrome (+2).
        for w, c in cnt.items():
            if w[0] == w[1] and c > 0:
                # We can use one such word in the middle
                has_middle = True
                break

        return length + (2 if has_middle else 0)

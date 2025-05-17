from typing import List

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        # dp[j] = length of best valid subsequence ending at j
        dp = [1] * n
        # prev[j] = index i before j in that subsequence, or -1 if j starts it
        prev = [-1] * n

        # helper: hamming distance == 1?
        def ham1(a: str, b: str) -> bool:
            # assume len(a) == len(b)
            diff = 0
            for x, y in zip(a, b):
                if x != y:
                    diff += 1
                    if diff > 1:
                        return False
            return diff == 1

        # bucket indices by word-length
        from collections import defaultdict
        by_len = defaultdict(list)
        for i, w in enumerate(words):
            by_len[len(w)].append(i)

        # for each length, do the O(n_ℓ^2 * ℓ) DP
        for ℓ, idxs in by_len.items():
            # ensure in increasing index order (subsequence)
            idxs.sort()
            for j in idxs:
                # try every possible predecessor i<j with same ℓ
                for i in idxs:
                    if i >= j:
                        break
                    # groups must differ
                    if groups[i] == groups[j]:
                        continue
                    # must be exactly 1 char diff
                    if not ham1(words[i], words[j]):
                        continue
                    # can extend
                    if dp[i] + 1 > dp[j]:
                        dp[j] = dp[i] + 1
                        prev[j] = i

        # find the end of the longest
        best_end = max(range(n), key=lambda i: dp[i])
        # reconstruct
        seq = []
        cur = best_end
        while cur != -1:
            seq.append(words[cur])
            cur = prev[cur]
        seq.reverse()
        return seq

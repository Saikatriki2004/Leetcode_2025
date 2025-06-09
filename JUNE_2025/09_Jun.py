class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_steps(curr, n):
            """ Count how many numbers are there between curr and curr + 1 in the lexicographical order. """
            steps = 0
            first = curr
            next_first = curr + 1
            while first <= n:
                steps += min(n + 1, next_first) - first
…                # We skip the whole range of `curr` and move to `curr + 1`
                k -= steps
                curr += 1
            else:
                # We go down to the next lexicographical level (curr * 10)
                k -= 1
                curr *= 10
        
        return curr

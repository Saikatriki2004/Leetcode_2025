from typing import List

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        L = 2 * n - 1
        ans = [0] * L
        used = [False] * (n + 1)  # used[i] is True if number i has been placed
        
        def backtrack(pos: int) -> bool:
            # Skip over positions already filled.
            while pos < L and ans[pos] != 0:
                pos += 1
            # If we've filled all positions, we've built a valid sequence.
            if pos == L:
                return True
            
            # Try numbers in descending order to get lexicographically largest sequence.
            for num in range(n, 0, -1):
                if not used[num]:
                    if num == 1:
                        # 1 occurs only once.
                        ans[pos] = 1
                        used[1] = True
                        if backtrack(pos + 1):
                            return True
                        # Backtrack:
                        ans[pos] = 0
                        used[1] = False
                    else:
                        # For num > 1, we need to place it at pos and at pos + num.
                        if pos + num < L and ans[pos] == 0 and ans[pos + num] == 0:
                            ans[pos] = num
                            ans[pos + num] = num
                            used[num] = True
                            if backtrack(pos + 1):
                                return True
                            # Backtrack:
                            ans[pos] = 0
                            ans[pos + num] = 0
                            used[num] = False
            return False
        
        backtrack(0)
        return ans

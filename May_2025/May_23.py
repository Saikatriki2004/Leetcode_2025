from typing import List

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        # 1) Compute base values and gains
        n = len(nums)
        base = sum(nums)
        gains = [ (nums[i] ^ k) - nums[i] for i in range(n) ]

        # 2) Partition gains
        pos = [g for g in gains if g > 0]
        neg = [g for g in gains if g < 0]
        zeros = gains.count(0)

        sum_pos = sum(pos)
        cpos = len(pos)

        # 3) If the count of positives is even, we can take them all:
        if cpos % 2 == 0:
            return base + sum_pos

        # 4) Otherwise, we need to fix parity:
        #    (a) If there's a zero-gain node, adding it costs nothing.
        if zeros > 0:
            return base + sum_pos

        #    (b) Otherwise, compare dropping the smallest positive vs. adding the largest negative
        #       (i) cost_drop = min(pos)
        #       (ii) cost_add  = -max(neg)   (since max(neg) is negative)
        cost_drop = min(pos) if pos else float('inf')
        cost_add  = -max(neg) if neg else float('inf')

        penalty = min(cost_drop, cost_add)
        return base + sum_pos - penalty

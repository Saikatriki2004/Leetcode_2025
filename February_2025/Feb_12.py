from typing import List

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # Helper function to compute the sum of digits of a number.
        def sum_digits(n: int) -> int:
            s = 0
            while n:
                s += n % 10
                n //= 10
            return s
        
        # Dictionary mapping digit sum to a pair: [largest, second largest]
        # We initialize second largest as -1 to denote that we haven't seen a second number yet.
        best = {}
        res = -1
        
        for num in nums:
            d = sum_digits(num)
            if d not in best:
                best[d] = [num, -1]
            else:
                if num > best[d][0]:
                    best[d][1] = best[d][0]
                    best[d][0] = num
                elif num > best[d][1]:
                    best[d][1] = num
        
        # For each group that has at least two numbers, update the answer.
        for d, pair in best.items():
            if pair[1] != -1:
                res = max(res, pair[0] + pair[1])
        
        return res

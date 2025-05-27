class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # 1) Sum of all numbers from 1 to n:
        total = n * (n + 1) // 2
        
        # 2) Number of multiples of m in [1..n]:
        k = n // m
        
        # 3) Sum of those multiples:
        #    m + 2m + ... + km = m * (1 + 2 + ... + k)
        #                   = m * k*(k+1)/2
        sum_div = m * k * (k + 1) // 2
        
        # 4) sum1 = total - sum_div, sum2 = sum_div
        #    We want sum1 - sum2 = (total - sum_div) - sum_div
        #                       = total - 2*sum_div
        return total - 2 * sum_div

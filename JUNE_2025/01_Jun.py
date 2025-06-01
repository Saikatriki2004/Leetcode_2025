class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # F(m) = binom(m+2, 2) if m >= 0, else 0
        def F(m: int) -> int:
            if m < 0:
                return 0
            return (m + 2) * (m + 1) // 2

        L = limit + 1
        total = F(n)
        one_violation = 3 * F(n - L)
        two_violation = 3 * F(n - 2*L)
        three_violation = F(n - 3*L)

        return total - one_violation + two_violation - three_violation

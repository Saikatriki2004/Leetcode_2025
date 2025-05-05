class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Handle the case for small n values
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:       
        return dp[n]

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        # Step 1: Initialize DP table for LCS
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Step 2: Fill DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # Step 3: Build the SCS
        i, j = m, n
        result = []
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                # Characters match, include once and move diagonally
                result.append(str1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                # Include from str1 and move up
                result.append(str1[i - 1])
                i -= 1
            else:
                # Include from str2 and move left
                result.append(str2[j - 1])
                j -= 1
        
        # Step 4: Append remaining characters from str1
        while i > 0:
            result.append(str1[i - 1])
            i -= 1
        
        # Step 5: Append remaining characters from str2
        while j > 0:
            result.append(str2[j - 1])
            j -= 1
        
        # Step 6: Reverse the result and join into a string
        return ''.join(result[::-1])

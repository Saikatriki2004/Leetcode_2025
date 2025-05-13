class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        
        # cur[c] = length that a single character chr(c + ord('a'))
        # expands to after *i* transformations; start with i=0 → length=1
        cur = [1] * 26
        
        # build up from i=1 to i=t
        for _ in range(t):
            nxt = [0] * 26
            # for 'a'..'y', next is just the count of the successor letter
            # i.e. f[i][c] = f[i-1][c+1]
            nxt[:25] = cur[1:]
            # for 'z' (index 25), we split into "ab" → counts of 'a' + 'b'
            nxt[25] = (cur[0] + cur[1]) % MOD
            cur = nxt
        
        # now cur[c] = how many chars a c‐letter becomes after t transforms
        ans = 0
        for ch in s:
            ans = (ans + cur[ord(ch) - ord('a')]) % MOD
        
        return ans

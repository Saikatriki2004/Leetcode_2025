class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7
        
        # 1) Generate all column-states (encoded 0,1,2 for R,G,B)
        #    that have no two equal colors vertically.
        states = []
        digits = []  # digits[i] is the base-3 list for states[i]
        for mask in range(3**m):
            col = []
            x = mask
            ok = True
            for _ in range(m):
                col.append(x % 3)
                x //= 3
            # check vertical adjacency
            for i in range(1, m):
                if col[i] == col[i-1]:
                    ok = False
                    break
            if ok:
                states.append(mask)
                digits.append(col)
        
        S = len(states)
        
        # 2) Precompute transitions: for each s, list all t such that
        #    digits[s][i] != digits[t][i] for every row i.
        trans = [[] for _ in range(S)]
        for i in range(S):
            di = digits[i]
            for j in range(S):
                dj = digits[j]
                for k in range(m):
                    if di[k] == dj[k]:
                        break
                else:
                    # no break ⇒ all rows differ
                    trans[i].append(j)
        
        # 3) DP arrays: dp_prev[s] = #ways up to current column ending in state s
        dp_prev = [1] * S  # column 1: every valid state once
        dp_cur = [0] * S
        
        # 4) Iterate columns 2..n
        for _ in range(1, n):
            for j in range(S):
                dp_cur[j] = 0
            for i in range(S):
                v = dp_prev[i]
                if not v:
                    continue
                for j in trans[i]:
                    dp_cur[j] = (dp_cur[j] + v) % MOD
            dp_prev, dp_cur = dp_cur, dp_prev
        
        # 5) Sum over last column states
        return sum(dp_prev) % MOD

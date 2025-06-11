class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        # map '0'..'4' to 0..4
        arr = [ord(c) - ord('0') for c in s]

        # pref[i][c] = count of char c in s[:i]
        pref = [[0]*5 for _ in range(n+1)]
        for i, x in enumerate(arr, start=1):
            for c in range(5):
                pref[i][c] = pref[i-1][c]
            pref[i][x] += 1

        ans = float('-inf')
        INF = 10**18

        for a in range(5):
            for b in range(5):
                if a == b:
                    continue

                # D[j] = freq_a(0..j) - freq_b(0..j)
                D = [pref[j][a] - pref[j][b] for j in range(n+1)]
                # state[j] = (parity of freq_a(0..j), parity of freq_b(0..j))
                state = [(pref[j][a] & 1, pref[j][b] & 1) for j in range(n+1)]

                # For each parity‐pair (pa,pb) we store:
                #   best_D[pa][pb]   = minimal D[i] seen so far
                #   best_prefb[pa][pb] = the pref[i][b] that goes with it
                best_D = [[INF, INF], [INF, INF]]
                best_prefb = [[INF, INF], [INF, INF]]

                # initialize with i=0
                p0a, p0b = state[0]
                best_D[p0a][p0b] = D[0]
                best_prefb[p0a][p0b] = pref[0][b]  # = 0

                for j in range(1, n+1):
                    i = j - k
                    if i >= 0:
                        pa, pb = state[i]
                        # if this prefix has a strictly smaller D, adopt it
                        if D[i] < best_D[pa][pb]:
                            best_D[pa][pb] = D[i]
                            best_prefb[pa][pb] = pref[i][b]

                    if j >= k:
                        pa_j, pb_j = state[j]
                        want_pa, want_pb = 1 - pa_j, pb_j
                        candD = best_D[want_pa][want_pb]
                        cand_prefb = best_prefb[want_pa][want_pb]
                        if candD != INF:
                            # enforce freq_b >= 2
                            if pref[j][b] - cand_prefb >= 2:
                                ans = max(ans, D[j] - candD)

        return ans

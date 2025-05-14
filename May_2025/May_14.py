class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        MOD = 10**9 + 7
        N = 26

        # 1) Build the one-step matrix M so that
        #    freq_next = M @ freq_current
        M = [[0]*N for _ in range(N)]
        for j in range(N):
            r = nums[j]
            for k in range(1, r+1):
                i = (j + k) % N
                M[i][j] += 1

        # 2) Matrix multiply and exponentiation (all mod MOD)
        def matmul(A, B):
            # C = A @ B
            C = [[0]*N for _ in range(N)]
            for i in range(N):
                for k in range(N):
                    if A[i][k]:
                        aik = A[i][k]
                        rowB = B[k]
                        c_row = C[i]
                        for j in range(N):
                            c_row[j] = (c_row[j] + aik * rowB[j]) % MOD
            return C

        def matpow(A, exp):
            # fast exponentiation
            R = [[1 if i==j else 0 for j in range(N)] for i in range(N)]
            while exp:
                if exp & 1:
                    R = matmul(R, A)
                A = matmul(A, A)
                exp >>= 1
            return R

        M_t = matpow(M, t)

        # 3) Build initial frequency vector
        freq0 = [0]*N
        for ch in s:
            freq0[ord(ch) - ord('a')] += 1

        # Apply M^t to freq0, then sum
        total = 0
        for i in range(N):
            # freq_t[i] = sum_j M_t[i][j] * freq0[j]
            acc = 0
            row = M_t[i]
            for j in range(N):
                if freq0[j]:
                    acc = (acc + row[j] * freq0[j]) % MOD
            total = (total + acc) % MOD

        return total

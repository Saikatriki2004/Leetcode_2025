class Solution:
    def countPairs(self, mat1, mat2, x):
        """
        mat1, mat2: two n x n matrices, each “flattened” in strictly ascending order row‐major.
        x: target sum.
        Returns the number of pairs (a from mat1, b from mat2) such that a + b == x.
        """
        n = len(mat1)
        N = n * n
        count = 0

        # i walks forward through mat1's flattened view; 
        # j walks backward through mat2's flattened view.
        i, j = 0, N - 1

        while 0 <= i < N and 0 <= j < N:
            a = mat1[i // n][i % n]
            b = mat2[j // n][j % n]
            s = a + b

            if s == x:
                count += 1
                i += 1
                j -= 1
            elif s < x:
                i += 1
            else:
                j -= 1

        return count

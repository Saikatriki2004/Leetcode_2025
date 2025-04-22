class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10**9 + 7
        m = n - 1
        
        # Precompute factorial and inverse factorial up to m + 14 (to handle exponents up to 14)
        max_fact = m + 14
        fact = [1] * (max_fact + 1)
        for i in range(1, max_fact + 1):
            fact[i] = fact[i-1] * i % MOD
        
        inv_fact = [1] * (max_fact + 1)
        inv_fact[max_fact] = pow(fact[max_fact], MOD-2, MOD)
        for i in range(max_fact - 1, -1, -1):
            inv_fact[i] = inv_fact[i+1] * (i+1) % MOD
        
        # Combination function
        def comb(n, k):
            if n < 0 or k < 0 or n < k:
                return 0
            return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD
        
        # Precompute the number of multiplicative compositions for each K up to maxValue
        max_K = maxValue
        comp = [0] * (max_K + 1)
        for K in range(1, max_K + 1):
            # Factorize K
            factors = {}
            x = K
            i = 2
            while i * i <= x:
                while x % i == 0:
                    factors[i] = factors.get(i, 0) + 1
                    x //= i
                i += 1
            if x > 1:
                factors[x] = factors.get(x, 0) + 1
            
            # Calculate product of combinations for each exponent
            res = 1
            for p, e in factors.items():
                c = comb(e + m - 1, e)
                res = res * c % MOD
            comp[K] = res
        
        # Compute prefix sums of comp
        sum_comp = [0] * (max_K + 1)
        for K in range(1, max_K + 1):
            sum_comp[K] = (sum_comp[K-1] + comp[K]) % MOD
        
        # Calculate the answer by iterating over all possible a
        ans = 0
        for a in range(1, maxValue + 1):
            T = maxValue // a
            if T == 0:
                continue
            if T > max_K:
                ans = (ans + sum_comp[max_K]) % MOD
            else:
                ans = (ans + sum_comp[T]) % MOD
        
        return ans

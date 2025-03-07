class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # If right < 2, no primes exist (smallest prime is 2)
        if right < 2:
            return [-1, -1]
        
        # Step 1: Sieve of Eratosthenes to find primes up to right
        is_prime = [True] * (right + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(right ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, right + 1, i):
                    is_prime[j] = False
        
        # Step 2: Collect primes in the range [left, right]
        primes = [i for i in range(left, right + 1) if is_prime[i]]
        
        # Step 3: Check if we have at least 2 primes
        if len(primes) < 2:
            return [-1, -1]
        
        # Step 4: Find the pair with minimal difference
        min_diff = float('inf')
        ans = [-1, -1]
        for i in range(len(primes) - 1):
            diff = primes[i + 1] - primes[i]
            if diff < min_diff:
                min_diff = diff
                ans = [primes[i], primes[i + 1]]
        
        return ans

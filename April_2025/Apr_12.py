import math
from itertools import product

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        if n == 1:
            return sum(1 for d in range(1, 10) if d % k == 0)
        
        m = (n + 1) // 2
        good_freqs = set()
        
        # Generate first half of palindromes
        for first_half in product(range(1, 10), *([range(10)] * (m - 1))):
            # Construct palindrome
            if n % 2 == 0:
                palindrome_digits = first_half + first_half[::-1]
            else:
                palindrome_digits = first_half[:-1] + (first_half[-1],) + first_half[:-1][::-1]
            
            p = int(''.join(map(str, palindrome_digits)))
            
            # Check if divisible by k
            if p % k == 0:
                freq = [0] * 10
                for d in palindrome_digits:
                    freq[d] += 1
                good_freqs.add(tuple(freq))
        
        total = 0
        for freq in good_freqs:
            total += self.permutations(freq)
        return total
    
    def permutations(self, freq):
        n = sum(freq)
        total_non_zero = sum(freq[1:])  # Number of non-zero digits
        if total_non_zero == 0:
            return 0  # No valid numbers possible
        perm = total_non_zero * math.factorial(n - 1)
        for f in freq:
            if f > 0:
                perm //= math.factorial(f)
        return perm

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        if not nums or k == 0:
            return 0
        
        max_x = max(nums)
        if max_x < 2:
            max_x = 2
        spf = list(range(max_x + 1))
        for i in range(2, int(max_x**0.5) + 1):
            if spf[i] == i:
                for j in range(i*i, max_x + 1, i):
                    if spf[j] == j:
                        spf[j] = i
        
        prime_scores = []
        for x in nums:
            if x == 1:
                prime_scores.append(0)
                continue
            factors = set()
            tmp = x
            while tmp != 1:
                p = spf[tmp]
                factors.add(p)
                while tmp % p == 0:
                    tmp //= p
            prime_scores.append(len(factors))
        
        n = len(nums)
        left_bound = [-1] * n
        stack = []
        for i in range(n):
            while stack and prime_scores[stack[-1]] < prime_scores[i]:
                stack.pop()
            if stack:
                left_bound[i] = stack[-1]
            else:
                left_bound[i] = -1
            stack.append(i)
        
        right_bound = [n] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and prime_scores[stack[-1]] <= prime_scores[i]:
                stack.pop()
            if stack:
                right_bound[i] = stack[-1]
            else:
                right_bound[i] = n
            stack.append(i)
        
        counts = [(i - left_bound[i]) * (right_bound[i] - i) for i in range(n)]
        sorted_pairs = sorted(zip(nums, counts), key=lambda x: (-x[0], x[1]))
        
        result = 1
        remaining_k = k
        for x, cnt in sorted_pairs:
            if remaining_k <= 0:
                break
            take = min(cnt, remaining_k)
            result = (result * pow(x, take, MOD)) % MOD
            remaining_k -= take
        
        return result

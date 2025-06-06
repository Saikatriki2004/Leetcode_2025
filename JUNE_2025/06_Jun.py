class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        min_suf = [''] * n
        min_suf[-1] = s[-1]
        for i in range(n - 2, -1, -1):
            min_suf[i] = s[i] if s[i] < min_suf[i + 1] else min_suf[i + 1]

        stack = []
        result = []
        i = 0

        while i < n:
            stack.append(s[i])
            i += 1
            while stack and (i == n or stack[-1] <= min_suf[i]):
                result.append(stack.pop())

        while stack:
            result.append(stack.pop())

        return "".join(result)

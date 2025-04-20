from collections import Counter

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        total = 0
        for x, freq in count.items():
            if x == 0:
                total += freq
            else:
                k = x + 1
                groups = (freq + k - 1) // k
                total += groups * k
        return total

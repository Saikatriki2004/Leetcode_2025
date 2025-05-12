from collections import Counter

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq = Counter(digits)
        ans = []
        
        # hundreds digit: 1–9 (no leading zero)
        # tens digit:   0–9
        # units digit:  only even digits (0,2,4,6,8)
        for h in range(1, 10):
            for t in range(0, 10):
                for u in (0, 2, 4, 6, 8):
                    # count how many times each digit appears in this candidate
                    need = Counter((h, t, u))
                    # check if we have enough of each in `digits`
                    if all(need[d] <= freq[d] for d in need):
                        ans.append(100*h + 10*t + u)
        
        return sorted(ans)

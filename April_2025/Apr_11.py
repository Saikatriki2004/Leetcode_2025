class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def is_symmetric(x):
            s = str(x)
            if len(s) == 2:
                return s[0] == s[1]
            elif len(s) == 4:
                return int(s[0]) + int(s[1]) == int(s[2]) + int(s[3])
            else:
                return False
        
        count = 0
        for x in range(low, high + 1):
            if is_symmetric(x):
                count += 1
        return count

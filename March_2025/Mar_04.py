class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            if n % 3 == 2:  # Check remainder when divided by 3
                return False
            n = n // 3  # Integer division to process next digit
        return True

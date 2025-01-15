class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        count = bin(num2).count('1')  # Count set bits in num2
        x = 0

        # Prioritize aligning bits with num1
        for i in range(31, -1, -1):
            if (num1 & (1 << i)) and count > 0:
                x |= (1 << i)
                count -= 1

        # If there are remaining bits to set, use least significant bits
        for i in range(32):
            if count > 0 and not (x & (1 << i)):
                x |= (1 << i)
                count -= 1

        return x

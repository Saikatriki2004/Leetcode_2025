class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        current = 1
        
        for _ in range(n):
            result.append(current)
            
            if current * 10 <= n:
                # Dive deeper by multiplying by 10
                current *= 10
            else:
                # Increment current or backtrack if needed
                if current >= n:
                    current //= 10
                current += 1
                while current % 10 == 0:
                    current //= 10
        
        return result

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        result = []
        
        def backtrack(current: str):
            # Base case: if the string length equals n, add it to the result.
            if len(current) == n:
                result.append(current)
                return
            # Try adding each character 'a', 'b', 'c'
            for ch in "abc":
                # We can only add ch if it is not equal to the last character.
                if not current or current[-1] != ch:
                    backtrack(current + ch)
        
        backtrack("")
        # If k is greater than the number of generated happy strings, return empty string.
        if k > len(result):
            return ""
        return result[k - 1]

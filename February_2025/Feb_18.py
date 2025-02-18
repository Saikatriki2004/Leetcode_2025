from typing import List

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        result = []
        stack = []
        n = len(pattern)
        
        # Process numbers from 1 to n+1
        for i in range(n + 1):
            # Push the current number as string onto the stack
            stack.append(str(i + 1))
            
            # If we reached the end of the pattern or the current pattern char is 'I'
            if i == n or pattern[i] == 'I':
                # Pop all elements from the stack and add them to the result
                while stack:
                    result.append(stack.pop())
        
        return "".join(result)

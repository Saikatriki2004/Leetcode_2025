class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        
        # If the length of the string is odd, it can't be valid
        if n % 2 != 0:
            return False
        
        # Left-to-right scan: ensure we never have more ')' than '('
        open_count = 0  # Count of open parentheses considering flexible ones
        for i in range(n):
            if locked[i] == '1':
                if s[i] == '(':
                    open_count += 1
                else:
                    open_count -= 1
            else:
                open_count += 1  # Treat as '(' to balance if needed
            
            if open_count < 0:
                return False  # More ')' than '(' at this point
        
        # Right-to-left scan: ensure we never have more '(' than ')'
        close_count = 0  # Count of close parentheses considering flexible ones
        for i in range(n - 1, -1, -1):
            if locked[i] == '1':
                if s[i] == ')':
                    close_count += 1
                else:
                    close_count -= 1
            else:
                close_count += 1  # Treat as ')' to balance if needed
            
            if close_count < 0:
                return False  # More '(' than ')' at this point
        
        return True

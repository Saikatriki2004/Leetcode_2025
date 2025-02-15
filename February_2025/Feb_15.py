class Solution:
    def punishmentNumber(self, n: int) -> int:
        # Helper function: given the string s, starting index pos,
        # and current sum, check if we can partition s (from pos to end)
        # so that the sum equals target.
        def canPartition(s: str, pos: int, current_sum: int, target: int) -> bool:
            # If we've reached the end of s, check if the accumulated sum equals target.
            if pos == len(s):
                return current_sum == target
            # If current_sum already exceeds target, we can prune this branch.
            if current_sum > target:
                return False
            
            # Try all possible splits: take substring s[pos:j+1] as the next number.
            for j in range(pos, len(s)):
                # Convert the substring to an integer.
                num = int(s[pos:j+1])
                # Recurse: if we can partition the remainder to reach target.
                if canPartition(s, j+1, current_sum + num, target):
                    return True
            return False

        total = 0
        
        # For each i in [1, n], check if i*i can be partitioned to sum to i.
        for i in range(1, n+1):
            square_str = str(i * i)
            if canPartition(square_str, 0, 0, i):
                total += i * i
        
        return total

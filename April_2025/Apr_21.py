class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        # Compute the prefix sums of the differences
        s = [0]
        current = 0
        for d in differences:
            current += d
            s.append(current)
        
        # Calculate the maximum lower bound and minimum upper bound for x
        max_lower = max(lower - x for x in s)
        min_upper = min(upper - x for x in s)
        
        # Determine the valid range for x
        a = max(lower, max_lower)
        b = min(upper, min_upper)
        
        return max(0, b - a + 1) if a <= b else 0

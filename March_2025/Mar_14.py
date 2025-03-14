class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        total = sum(candies)
        if total < k:
            return 0
        
        low = 1
        high = max(candies)
        while low <= high:
            mid = (low + high) // 2
            sub_piles = sum(c // mid for c in candies)
            if sub_piles >= k:
                low = mid + 1
            else:
                high = mid - 1
        return high

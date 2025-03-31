class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0
        
        n = len(weights)
        split_values = []
        for i in range(n - 1):
            split_values.append(weights[i] + weights[i + 1])
        
        split_values.sort()
        
        max_sum = sum(split_values[-(k-1):])
        min_sum = sum(split_values[:k-1])
        
        return max_sum - min_sum

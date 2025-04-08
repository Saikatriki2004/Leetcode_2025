class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        for k in range(n + 1):
            if k == n or len(set(nums[k:])) == len(nums[k:]):
                return (k + 2) // 3

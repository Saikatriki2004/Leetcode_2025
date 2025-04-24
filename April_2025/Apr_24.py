class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        K = len(set(nums))
        n = len(nums)
        count = 0
        
        for i in range(n):
            distinct = set()
            for j in range(i, n):
                distinct.add(nums[j])
                if len(distinct) == K:
                    count += n - j
                    break
        
        return count

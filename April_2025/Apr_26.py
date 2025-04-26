class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        answer = 0
        last_invalid = -1
        last_minK_pos = -1
        last_maxK_pos = -1
        
        for j in range(len(nums)):
            if nums[j] < minK or nums[j] > maxK:
                last_invalid = j
            else:
                if nums[j] == minK:
                    last_minK_pos = j
                if nums[j] == maxK:
                    last_maxK_pos = j
            answer += max(0, min(last_minK_pos, last_maxK_pos) - last_invalid)
        
        return answer

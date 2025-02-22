from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        result = []
        for i in range(n):
            # Flip the i-th character of the i-th string.
            result.append('1' if nums[i][i] == '0' else '0')
        return ''.join(result)

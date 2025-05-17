class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Sort nums in-place so that all 0’s come first, then 1’s, then 2’s.
        Uses the Dutch National Flag algorithm in a single pass.
        """

        # low   : boundary for next 0 (red)
        # mid   : current element under consideration
        # high  : boundary for next 2 (blue)
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                # swap nums[mid] (a 0) into the "red" region at low
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # 1’s belong in the middle—just advance
                mid += 1
            else:  # nums[mid] == 2
                # swap nums[mid] (a 2) into the "blue" region at high
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        # at the end: [0…low-1]=0, [low…high]=1, [high+1…end]=2

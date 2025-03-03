class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        left = []
        middle = []
        right = []
        for num in nums:
            if num < pivot:
                left.append(num)
            elif num == pivot:
                middle.append(num)
            else:
                right.append(num)
        return left + middle + right

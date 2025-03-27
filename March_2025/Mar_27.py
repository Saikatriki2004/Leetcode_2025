class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return -1
        
        # Step 1: Find the dominant element using Boyer-Moore
        candidate = None
        counter = 0
        for num in nums:
            if counter == 0:
                candidate = num
            if num == candidate:
                counter += 1
            else:
                counter -= 1
        x = candidate
        
        # Step 2: Compute total count of the dominant element
        total_count = sum(1 for num in nums if num == x)
        
        # Step 3: Find the minimum index for a valid split
        left_count = 0
        for i in range(n - 1):
            if nums[i] == x:
                left_count += 1
            right_count = total_count - left_count
            if left_count > (i + 1) // 2 and right_count > (n - i - 1) // 2:
                return i
        
        # Step 4: No valid split found
        return -1

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        # Sort so nums[0] <= nums[1] <= nums[2]
        a, b, c = sorted(nums)
        
        # Triangle inequality: sum of any two sides must exceed the third
        if a + b <= c:
            return "none"
        
        # All three equal → equilateral
        if a == c:
            return "equilateral"
        # Exactly two equal → isosceles
        if a == b or b == c:
            return "isosceles"
        # Otherwise → scalene
        return "scalene"

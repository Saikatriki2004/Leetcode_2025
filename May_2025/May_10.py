from typing import List

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1_non_zero, zeros1 = 0, 0
        for num in nums1:
            if num == 0:
                zeros1 += 1
            else:
                sum1_non_zero += num
        
        sum2_non_zero, zeros2 = 0, 0
        for num in nums2:
            if num == 0:
                zeros2 += 1
            else:
                sum2_non_zero += num
        
        if zeros1 > 0 and zeros2 > 0:
            s1_min = sum1_non_zero + zeros1
            s2_min = sum2_non_zero + zeros2
            return max(s1_min, s2_min)
        elif zeros1 == 0 and zeros2 == 0:
            return sum1_non_zero if sum1_non_zero == sum2_non_zero else -1
        else:
            if zeros1 == 0:
                required_b = sum1_non_zero - sum2_non_zero
                if required_b >= zeros2 and required_b >= 0:
                    return sum1_non_zero
                else:
                    return -1
            else:
                required_a = sum2_non_zero - sum1_non_zero
                if required_a >= zeros1 and required_a >= 0:
                    return sum2_non_zero
                else:
                    return -1

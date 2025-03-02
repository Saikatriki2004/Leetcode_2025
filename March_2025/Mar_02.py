class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        # Initialize the result list and pointers
        result = []
        i, j = 0, 0
        
        # Merge arrays while both pointers are within bounds
        while i < len(nums1) and j < len(nums2):
            if nums1[i][0] == nums2[j][0]:
                # Ids are equal, sum the values and add to result
                result.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i += 1
                j += 1
            elif nums1[i][0] < nums2[j][0]:
                # Id in nums1 is smaller, add it to result
                result.append(nums1[i])
                i += 1
            else:
                # Id in nums2 is smaller, add it to result
                result.append(nums2[j])
                j += 1
        
        # Add remaining elements from nums1, if any
        while i < len(nums1):
            result.append(nums1[i])
            i += 1
        
        # Add remaining elements from nums2, if any
        while j < len(nums2):
            result.append(nums2[j])
            j += 1
        
        return result

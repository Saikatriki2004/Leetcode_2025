from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        prefix_common_array = []
        seen = set()
        count = 0
        
        for i in range(n):
            # Add the current elements of A and B to the seen set
            if A[i] in seen:
                count += 1
            else:
                seen.add(A[i])
            
            if B[i] in seen:
                count += 1
            else:
                seen.add(B[i])
            
            # Append the current count to the result array
            prefix_common_array.append(count)
        
        return prefix_common_array

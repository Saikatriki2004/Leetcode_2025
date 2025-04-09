import math

class Solution:
  def minOperations(self, nums: List[int], k: int) -> int:
    for x in nums:
      if x < k:
        return -1
    unique_values_greater_than_k = set()
    for x in nums:
      if x > k:
        unique_values_greater_than_k.add(x)
    return len(unique_values_greater_than_k)

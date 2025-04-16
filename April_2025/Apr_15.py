from typing import List

class FenwickTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (self.n + 1)  # 1-based indexing

    def update(self, index, delta):
        # Convert 0-based index to 1-based
        i = index + 1
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def query(self, index):
        # Sum from 0 to index (0-based)
        res = 0
        i = index + 1  # Convert to 1-based
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        pos1 = [0] * n
        pos2 = [0] * n
        for i in range(n):
            pos1[nums1[i]] = i
            pos2[nums2[i]] = i

        left_counts = [0] * n
        right_counts = [0] * n

        # Compute left counts
        ft_left = FenwickTree(n)
        for x in sorted(range(n), key=lambda x: pos1[x]):
            current_pos2 = pos2[x]
            left = ft_left.query(current_pos2 - 1)
            left_counts[x] = left
            ft_left.update(current_pos2, 1)

        # Compute right counts
        ft_right = FenwickTree(n)
        for x in sorted(range(n), key=lambda x: -pos1[x]):
            current_pos2 = pos2[x]
            total = ft_right.query(n - 1)
            less_or_equal = ft_right.query(current_pos2)
            right_counts[x] = total - less_or_equal
            ft_right.update(current_pos2, 1)

        total = 0
        for x in range(n):
            total += left_counts[x] * right_counts[x]
        return total

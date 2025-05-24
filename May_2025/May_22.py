from typing import List
import heapq

class Fenwick:
    """Fenwick tree (BIT) supporting point‐query, range‐update."""
    def __init__(self, n: int):
        self.n = n
        self.fw = [0] * (n+1)
    def add(self, i: int, v: int):
        """Add v at index i (0-based)."""
        i += 1
        while i <= self.n:
            self.fw[i] += v
            i += i & -i
    def prefix_sum(self, i: int) -> int:
        """Sum[0..i], 0-based inclusive."""
        i += 1
        s = 0
        while i > 0:
            s += self.fw[i]
            i -= i & -i
        return s

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n, q = len(nums), len(queries)

        # 1) Quick check: can the total available coverage ever meet nums[j]?
        diff = [0]*(n+1)
        for l, r in queries:
            diff[l] += 1
            if r+1 < n: 
                diff[r+1] -= 1
        cur = 0
        for j in range(n):
            cur += diff[j]
            if cur < nums[j]:
                return -1   # not enough total queries covering j

        # 2) Prepare intervals sorted by left endpoint
        ivals = sorted(queries, key=lambda x: x[0])
        ptr = 0

        # 3) Fenwick for range updates + point queries of "how many kept intervals cover j so far"
        bit = Fenwick(n)

        # 4) Max-heap of candidate intervals (by farthest right endpoint)
        #    We store (-r, l) so heapq gives us the interval with the largest r.
        heap = []
        kept = 0

        # 5) Sweep j = 0..n-1
        for j in range(n):
            # push all intervals whose l <= j
            while ptr < q and ivals[ptr][0] <= j:
                l, r = ivals[ptr]
                heapq.heappush(heap, (-r, l))
                ptr += 1

            # pop out any intervals that no longer cover j (r < j)
            while heap and -heap[0][0] < j:
                heapq.heappop(heap)

            # how many times is j already covered by the intervals we've kept?
            covered = bit.prefix_sum(j)

            # if we still need more coverage at j, pick intervals greedily
            while covered < nums[j]:
                if not heap:
                    # no more intervals can cover j, so impossible
                    return -1

                r, l = heapq.heappop(heap)
                r = -r
                # keep this interval: update coverage +1 on [l..r]
                bit.add(l, 1)
                if r+1 < n:
                    bit.add(r+1, -1)

                kept += 1
                covered += 1

        # 6) We kept 'kept' intervals; we can remove the rest
        return q - kept

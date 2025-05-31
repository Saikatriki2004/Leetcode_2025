import heapq

class Solution:
    def kthSmallest(self, matrix, k):

        n = len(matrix)
        # A min-heap of tuples (value, row_index, col_index)
        min_heap = []
        
        # 1) Seed the heap with the first element of each row (col = 0).
        for r in range(n):
            # (value, row, col)
            heapq.heappush(min_heap, (matrix[r][0], r, 0))
        
        # 2) Pop (k-1) times; each time we pop (val, r, c), we push (matrix[r][c+1], r, c+1) if c+1 < n.
        for _ in range(k - 1):
            val, r, c = heapq.heappop(min_heap)
            if c + 1 < n:
                heapq.heappush(min_heap, (matrix[r][c + 1], r, c + 1))
        
        # 3) The top of the heap is now the k-th smallest.
        return min_heap[0][0]

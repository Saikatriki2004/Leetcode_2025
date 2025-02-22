from collections import defaultdict
import heapq
from typing import List

class NumberContainers:
    def __init__(self):
        # Maps index -> current number in that container.
        self.index_to_number = {}
        # Maps number -> min-heap of indices that hold that number.
        self.num_to_heap = defaultdict(list)
    
    def change(self, index: int, number: int) -> None:
        # Update the container at the given index to the new number.
        self.index_to_number[index] = number
        # Push the index into the heap for the given number.
        heapq.heappush(self.num_to_heap[number], index)
    
    def find(self, number: int) -> int:
        # If there is no container with the given number, return -1.
        if number not in self.num_to_heap:
            return -1
        
        heap = self.num_to_heap[number]
        # Remove stale indices from the heap.
        while heap and self.index_to_number.get(heap[0], None) != number:
            heapq.heappop(heap)
        
        # Return the smallest index if available; otherwise, return -1.
        return heap[0] if heap else -1

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index, number)
# param_2 = obj.find(number)

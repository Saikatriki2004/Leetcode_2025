from collections import deque
from typing import List

class Solution:
    def maxCandies(self, status: List[int], 
                   candies: List[int], 
                   keys: List[List[int]], 
                   containedBoxes: List[List[int]], 
                   initialBoxes: List[int]) -> int:
        n = len(status)
        
        # (1) “available” = all boxes we currently hold (opened or unopened)
        available = set(initialBoxes)
        # (2) “keys_set” = all box‐labels for which we have a key
        keys_set = set()
        # (3) “opened” = boxes we have already opened & taken candies from
        opened = set()
        # (4) “waiting” = boxes we hold but cannot open yet (locked, no key)
        waiting = set()
        # (5) “q” = BFS queue of boxes that are openable right now
        q = deque()
        
        # Initialize: for each box in initialBoxes, either open it or put in waiting.
        for b in initialBoxes:
            if status[b] == 1:
                q.append(b)
            else:
                waiting.add(b)
        
        total = 0
        
        while q:
            b = q.popleft()
            # If we already opened this box, skip
            if b in opened:
                continue
            
            # (A) Open box b now:
            opened.add(b)
            total += candies[b]
            
            # (B) Collect any keys inside box b
            for k in keys[b]:
                if k not in keys_set:
                    keys_set.add(k)
                    # If we happened to already have box “k” in waiting, we can now open it:
                    if k in waiting:
                        waiting.remove(k)
                        q.append(k)
            
            # (C) Collect any boxes that were contained inside box b
            for y in containedBoxes[b]:
                if y not in available:
                    available.add(y)
                    # If box y is already openable (status[y] = 1 or we have its key), enqueue it.
                    if status[y] == 1 or (y in keys_set):
                        q.append(y)
                    else:
                        waiting.add(y)
                # If y was already in available, we’ve enqueued or are waiting for it elsewhere.
        
        return total

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        possible_swaps = []
        candidates = {tops[0], bottoms[0]}
        
        for x in candidates:
            top_count = 0
            top_valid = True
            for i in range(len(tops)):
                if tops[i] != x:
                    if bottoms[i] == x:
                        top_count += 1
                    else:
                        top_valid = False
                        break
            if top_valid:
                possible_swaps.append(top_count)
            
            bottom_count = 0
            bottom_valid = True
            for i in range(len(bottoms)):
                if bottoms[i] != x:
                    if tops[i] == x:
                        bottom_count += 1
                    else:
                        bottom_valid = False
                        break
            if bottom_valid:
                possible_swaps.append(bottom_count)
        
        return min(possible_swaps) if possible_swaps else -1

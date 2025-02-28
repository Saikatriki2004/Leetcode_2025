class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        # Map each value to its index for quick lookup
        val_to_idx = {arr[i]: i for i in range(n)}
        # DP table: dp[(j,k)] is length of sequence ending at arr[j], arr[k]
        dp = {}
        max_length = 0
        
        # Consider each element as potential end of sequence (k)
…                        dp[(j, k)] = dp[(i, j)] + 1
                    # Otherwise, start new sequence of length 3
                    else:
                        dp[(j, k)] = 3
                    # Update maximum length found
                    max_length = max(max_length, dp[(j, k)])
        
        # Return max_length if we found a valid sequence, else 0
        return max_length if max_length >= 3 else 0

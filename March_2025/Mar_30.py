from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Create a dictionary to store the last occurrence of each character
        last_occurrence = {char: idx for idx, char in enumerate(s)}
        
        result = []
        start = 0  # Start index of the current partition
        end = 0     # End index of the current partition
        
        for current_idx, char in enumerate(s):
            # Update the end to be the maximum of the current end and the last occurrence of the current character
            end = max(end, last_occurrence[char])
            
            # If current index reaches the end of the current partition, finalize the partition
            if current_idx == end:
                # Calculate the length of the current partition
                result.append(end - start + 1)
                # Move the start to the next index for the next partition
                start = current_idx + 1
        
        return result

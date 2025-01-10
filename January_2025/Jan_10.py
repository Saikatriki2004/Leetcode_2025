from collections import Counter
from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def merge_counts(words):
            combined_count = Counter()
            for word in words:
                word_count = Counter(word)
                for char in word_count:
                    combined_count[char] = max(combined_count[char], word_count[char])
            return combined_count
        
        # Calculate the maximum frequency of each character required by words2
        required_count = merge_counts(words2)
        
        result = []
        
        for word in words1:
            word_count = Counter(word)
            if all(word_count[char] >= required_count[char] for char in required_count):
                result.append(word)
        
        return result

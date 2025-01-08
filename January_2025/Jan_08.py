class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        
        # Iterate over all pairs (i, j) with i < j
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                # Check if words[i] is both a prefix and a suffix of words[j]
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    count += 1
        
        return count

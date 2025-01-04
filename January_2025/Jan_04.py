class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first_occurrence = {}
        last_occurrence = {}
        
        for i, char in enumerate(s):
            if char not in first_occurrence:
                first_occurrence[char] = i
            last_occurrence[char] = i
        
        unique_palindromes = set()
        
        for char in first_occurrence:
            start = first_occurrence[char]
            end = last_occurrence[char]
            if end - start > 1:
                middle_chars = set(s[start + 1:end])
                for middle_char in middle_chars:
                    unique_palindromes.add((char, middle_char, char))
        
        return len(unique_palindromes)

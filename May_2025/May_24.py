from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        """
        Returns the list of indices i such that words[i] contains the character x.
        """
        result = []
        for i, w in enumerate(words):
            if x in w:
                result.append(i)
        return result

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    print(sol.findWordsContaining(["leet","code"], "e"))      # [0, 1]
    print(sol.findWordsContaining(["abc","bcd","aaaa","cbc"], "a"))  # [0, 2]
    print(sol.findWordsContaining(["abc","bcd","aaaa","cbc"], "z"))  # []

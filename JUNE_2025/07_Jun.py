class Solution:
    def clearStars(self, s: str) -> str:
        n = len(s)
        # pos[c] will be a stack of indices where character chr(c + 97) occurs
        pos = [[] for _ in range(26)]
        deleted = [False] * n

        for i, ch in enumerate(s):
            if ch == '*':
                # find the smallest letter still available (c = 0 for 'a', …, 25 for 'z')
                for c in range(26):
                    if pos[c]:
                        # pop its rightmost occurrence
                        j = pos[c].pop()
                        deleted[j] = True
                        break
                # we simply skip storing the '*' itself
            else:
                # push index onto its bucket
                pos[ord(ch) - 97].append(i)

        # rebuild the answer skipping '*' and any deleted letters
        ans = []
        for i, ch in enumerate(s):
            if ch != '*' and not deleted[i]:
                ans.append(ch)
        return ''.join(ans)

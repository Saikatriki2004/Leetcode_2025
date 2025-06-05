class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # Union–Find over 26 letters (0='a', 1='b', ..., 25='z')
        parent = list(range(26))
        
        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(a: int, b: int) -> None:
            ra = find(a)
            rb = find(b)
            if ra == rb:
                return
            # Always attach the larger root under the smaller root,
            # so that the representative is the lexicographically smallest.
            if ra < rb:
                parent[rb] = ra
            else:
                parent[ra] = rb
        
        # Build unions from s1[i] == s2[i]
        for c1, c2 in zip(s1, s2):
            i1 = ord(c1) - ord('a')
            i2 = ord(c2) - ord('a')
            union(i1, i2)
        
        # For each character in baseStr, replace with the root (smallest char in its class)
        ans_chars = []
        for c in baseStr:
            idx = ord(c) - ord('a')
            root = find(idx)
            ans_chars.append(chr(root + ord('a')))
        
        return "".join(ans_chars)

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def atleastk(k):
            vow={i:0 for i in 'aeiou'}
            cons=0
            ans=0
            l=0
            for r,c in enumerate(word):
                if c in 'aeiou': vow[c]+=1
                else: cons+=1
                while cons>=k and all(i>0 for i in vow.values()):
                    ans+=len(word)-r
                    if word[l] in 'aeiou': vow[word[l]]-=1
                    else:  cons-=1
                    l+=1
            return ans
        return atleastk(k)-atleastk(k+1)

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        li = s.split()
        res = ''
        for i in range(k):
            res += li[i]+" "
        return res.strip()
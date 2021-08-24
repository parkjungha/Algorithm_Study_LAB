class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split()
        ans = len(text) # 총 단어의 개수
        for i in text:
            for j in brokenLetters: 
                if j in i:
                    ans -= 1
                    break
        return ans
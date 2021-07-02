'''
Idea (가 떠오르지 않아서 구글링함..)

words라는 리스트의 element 개수를 n이라고 할 때,
words에 등장하는 모든 character에 대해서 등장하는 총 빈도수를 세었을 때, 
그 빈도수가 n개거나 n의 배수가 되어야함
이 조건이 만족되어야만 몇 번이든 이동했을 때 모두 같은 문자열을 만들 수 있음

'''

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        chars = "".join(words)
        
        from collections import Counter
        freq = Counter(chars).values()
        
        for i in freq:
            if i%n != 0:
                return False
        return True
        
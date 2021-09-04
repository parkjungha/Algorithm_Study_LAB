#1-1.

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        
        # Convert
        converted = ''
        for i in range(len(s)):
            converted += str(alphabet.index(s[i]) + 1) 
        
        # Transform * k times
        for i in range(k):
            converted = str(sum([int(j) for j in converted]))
        return converted
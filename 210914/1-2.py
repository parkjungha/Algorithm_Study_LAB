class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        answer = ''
        
        for i, num in enumerate(nums):
            if num[i] == '0':
                answer += '1'
            else:
                answer += '0'
            
        return answer
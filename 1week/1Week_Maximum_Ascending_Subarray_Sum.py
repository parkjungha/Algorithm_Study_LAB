class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxVal = 0
        temp = [nums[0]]
        n = len(nums)
        for i in range(n-1):
            if nums[i]<nums[i+1]:
                temp.append(nums[i+1])
                print(temp)
            else:
                maxVal = max(maxVal,sum(temp)) 
                temp = [nums[i+1]] 

        return max(maxVal,sum(temp))
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        minVal = 100000000
        for idx,val in enumerate(nums):
            if val == target:
                minVal = min(minVal, abs(idx-start))
        return minVal
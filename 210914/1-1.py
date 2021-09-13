class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smallest = min(nums)
        largest = max(nums)
        for i in range(smallest, 0, -1):
            if largest % i == 0 and smallest % i == 0: # 나누어지면
                return i
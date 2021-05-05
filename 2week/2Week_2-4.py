class Solution:
    def thirdMax(self,nums):
        nums = sorted(list(set(nums)),reverse=True) # 중복제거하고 내림차순으로 정렬함
        if len(nums)<3: # 3보다 작으면 젤 큰 값
            return nums[0]
        else: return nums[2]

        
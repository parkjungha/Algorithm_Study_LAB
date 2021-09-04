
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        while True:
            swap = 0 # 더이상 바꿀게 하나도 없을때까지 계속 처음부터 돌면서 반복함 
            for i in range(1,len(nums)-1):
                if nums[i] == (nums[i-1] + nums[i+1]) / 2:
                    temp = nums[i]
                    nums[i] = nums[i+1]
                    nums[i+1] = temp
                    swap += 1
            if swap == 0:
                break
                    
        return nums
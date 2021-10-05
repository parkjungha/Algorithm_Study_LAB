# 시간초과
class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        sumOfBeauty = 0

        for i in range(1, len(nums)-1):
            score = 2
            for j in range(0,i):
                if nums[j] >= nums[i]: # nums[j] < nums[i] 조건 불만족
                    score -= 1 
                    break
                for k in range(i+1, len(nums)): # nums[i] < nums[k] 조건 불만족
                    if nums[k] <= nums[i]:
                        score -= 1
                        break

            if score == 2:
                sumOfBeauty += 2
            elif nums[i - 1] < nums[i] and nums[i] < nums[i + 1]:
                sumOfBeauty += 1

        return sumOfBeauty

# 정답
# 특정 요소의 오른쪽에 있는 값들의 최솟값보다 작다면 
# 특정 요소의 왼쪽에 있는 모든 값의 최댓값보다 크다면 

def sumOfBeauties(nums):
    n =len(nums)
    right = [nums[-1]]*n 
    for i in range(n-2, 0, -1): # 오른쪽에서 왼쪽으로 (양쪽 끝 빼고)
        right[i] = min(nums[i+1], right[i+1])

    maxi = nums[0] 
    sumOfBeauty = 0
    for i in range(1, n-1): # 왼쪽에서 오른쪽으로
        if nums[i] < right[i] and nums[i] > maxi:
            sumOfBeauty += 2
        elif nums[i] < nums[i+1] and nums[i] > nums[i-1]:
            sumOfBeauty += 1
        maxi = max(maxi, nums[i])

    return sumOfBeauty


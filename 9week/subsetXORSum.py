class Solution:
	def subsetXORSum(self, nums: List[int]) -> int:
        
		allSubset = [] # 모든 subset을 저장할 list
		ans = 0

		for i in range(len(nums)+1):
			for j in combinations(nums,i): 
				allSubset.append(j)
                
		for subset in allSubset[1:]: # 첫번째 공집합 빼고 나머지 모든 subset에 대해서 반복함
			ans += reduce(lambda a,b : a^b, subset) # XOR 연산. 
		return(ans)
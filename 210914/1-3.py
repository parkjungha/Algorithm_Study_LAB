'''
파이썬은 메모이제이션을 쉽게 적용할 수 있는 데코레이터를 제공한다. functools 모듈의 lru_cache 데코레이터가 이것이다. 이 데코레이터를 붙이면 함수의 실행 결과를 캐싱해준다.
@cache decorator는 함수가 이전에 받았던 인수에 대한 결과값을 caching하는 것 입니다. 메모리는 좀 소모되겠지만, 중복 연산을 피할 수 있습니다.

'''

class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        @cache
        def dfs(row, currSum):
            if row == len(mat):
                return abs(target - currSum)
            
            tmp = float('inf')
            for col in mat[row]:
                tmp = min(tmp, dfs(row+1, col + currSum))
                if tmp == 0: # target이랑 같아지면 바로 return.
                    return 0
            
            return tmp
        
        for i in range(len(mat)):
            mat[i].sort()
        return dfs(0, 0)
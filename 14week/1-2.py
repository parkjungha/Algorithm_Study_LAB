class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        rungs.insert(0,0) # 시작점 0
        ans=0
        
        for i in range(len(rungs)-1):
            gap = rungs[i+1]-rungs[i]
            if(gap > dist):
                if(gap % dist==0):
                    ans += (gap//dist)-1
                else:
                    ans += gap//dist
        return ans
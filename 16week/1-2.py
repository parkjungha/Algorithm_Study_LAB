class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        replaced = False
        res = ""
        
        for idx, val in enumerate(num):
            
            intVal = int(val)
            
            if change[intVal] > intVal:
                res += str(change[intVal])
                replaced = True
                
            elif change[intVal] == intVal:
                res += val
                
            else: 
                if replaced:
                    return res + num[idx:]
                res += val
                
        return res
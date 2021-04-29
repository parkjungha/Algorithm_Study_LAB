

def arraySign(nums):
    res = 1
    for n in nums:
        res *= n
    
    if res>0:
        return 1
    elif res<0:
        return -1
    else:
        return 0

print(arraySign([-1,-2,-3,-4,3,2,1]))

print(arraySign([1,5,0,2,-3]))

print(arraySign([-1,1,-1,1,-1]))
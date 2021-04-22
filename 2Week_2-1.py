from copy import deepcopy

example = [[1,2,3],[4,5,6],[7,8,9]]

# 규칙: 90"회전 하기 전의 행렬을 Before, 하고난 후의 행렬을 After이라고 했을 때,
# 각 칸은 아래와 같은 규칙으로 바뀜
# After의 행 번호 = Before의 열 번호
# After의 열 번호 = (N-1)-Before의 행 번호

def rotate_90(array):
    n = len(array)
    temp = deepcopy(array)
    for i in range(n):
        for j in range(n):
            temp[j][(n-1)-i] = array[i][j]
    return temp

def rotate_180(array):
    return rotate_90(rotate_90(array)) # 180도 회전은 90도 회전을 두번 한것

def rotate_270(array):
    return rotate_90(rotate_90(rotate_90(array)))

print(rotate_90(example))
print(rotate_180(example))
print(rotate_270(example))
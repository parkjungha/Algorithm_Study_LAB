
n = int(input())
height = list(map(int,input().split()))

stack = [] # 인덱스 담기
answer = [0]*n 

for i in range(n): # 탑의 왼쪽부터 오른쪽부터 순회
    while stack and height[stack[-1]] < height[i]: # 스택이 비어있지 않고, stack의 top값의 높이가 현재 값보다 더 작을 때.
        stack.pop() # 왼쪽에 있는 더 작은 값은 필요 없으므로 삭제
    if stack: # 스택에 값이 있으면 (스택이 비어있으면 default값인 0으로 남아있음)
        answer[i] = stack[-1]+1 # top 값 (index차이 때문에 1 더해줌)
    stack.append(i) # stack에 현재값의 인덱스 추가.

for i in answer:
    print(i,end=" ")

# 6 9 5 7 4
class Stack():
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if self.is_empty():
            raise EmptyStackError
        else:
            return self.data.pop()

    def peek(self):
        if self.is_empty():
            raise EmptyStackError
        else:
            return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

stack = Stack() # 정렬할 스택
stack.push(10)
stack.push(30)
stack.push(90)
stack.push(50)
stack.push(20)

def stackSort(stack):
    stackTemp = Stack() # 정렬을 위해 사용되는 임시 스택
    while stack.is_empty() == False: # 스택이 빌 때까지 반복
        temp = stack.pop() 
        while stackTemp.is_empty() == False and stackTemp.peek() > temp: # 임시스택의 top값이 스택의 top값보다 클 때
            stack.push(stackTemp.pop()) # 임시스택의 top 값을 stack에 넣어줌
        stackTemp.push(temp) # 임시스택의 top 값이 스택의 top값보다 작을때는 임시스택에 스택의 top값을 넣어줌

    while stackTemp.is_empty() == False: # 반복문을 다 돌고나서 임시스택이 아직 값이 남아있으면
        stack.push(stackTemp.pop()) # 스택에 다 넣어줌
               
    print(stack.data)
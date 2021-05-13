
''' 
Idea: min값을 저장할 minStack을 만들어서, 스택 push, pop 연산할 때 마다 최소값을 비교하여 minStack에 업데이트 해준다

min 연산을 O(1)시간에 동작하게 할 방법이 도저히 떠오르지 않아서 구글링으로 아이디어를 얻어서 구현함..
처음에는 그냥 minVal 라는 int형 변수를 써서 저장해도 될텐데 왜 굳이 minStack을 만드나 의아했는데
push할 때는 문제가 없지만 pop할 때 삭제되는 값이 만약 최소값이었다면 그 전의 최소값으로 다시 바꾸어줘야 하는데
이때 min Stack을 사용하는게 편리하다는 것을 알게 됨

'''

class EmptyStackError(Exception):
  pass

class Stack():
  def __init__(self):
    self.data = []
    self.minStack = []

  def is_empty(self):
    return len(self.data) == 0
  
  def top(self):
    if self.is_empty():
      raise EmptyStackError
    return self.data[-1]

  def pop(self):
    if self.is_empty():
      raise EmptyStackError

    if self.data.pop() == self.minStack[-1]: # Pop할 값이 최소값이라면
      self.minStack.pop() # minStack에서도 pop해줌. 

    return self.data.pop()

  def push(self, x):
    self.data.append(x)

    if not self.minStack or self.minStack[-1] > x: # minStack이 비어있거나, 새로 들어온 데이터가 minStack의 Top값보다 작으면
      self.minStack.append(x) # min 값 업데이트 (minStack에 push)

  # Min 함수 !!!
  def min(self):
    if not self.minStack: # minStack 이 비어있으면 return None
      return None
    return self.minStack[-1] # minStack 의 top 값



# Test 

stack = Stack()
stack.push(10)
stack.push(100)
stack.push(1)
stack.push(-10)

print(stack.minStack) # [10, 1, -10]
print(stack.min()) # -10

stack.pop() 
print(stack.min()) # 1
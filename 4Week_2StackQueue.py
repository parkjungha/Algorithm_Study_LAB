'''

Idea: Stack1, Stack2 두개의 스택을 사용해서
Stack1은 Enqueue를 위해서, Stack2는 Dequeue를 위해서 사용함
Dequeue할 때, Stack1에 있는 원소 하나하나에 대해서 pop해서 바로 Stack2에 push하면
순서가 바뀌어서 들어가게 됨. 근데 이것은 Stack2가 비어있을 때만 수행해야하고,
Stack2에 원소가 남아있으면 그 원소 pop하면 됨
Enqueue는 그냥 Stack1에 append.

'''

class EmptyStackError(Exception):
  pass

class MyQueue():

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        self.stack1.append(x)

    def pop(self):
        if not self.stack2 and not self.stack1: # 둘다 비어있을 때
            raise EmptyStackError

        if not self.stack2: # Stack2 가 비어있다면
            while self.stack1: # Stack1에 있는거 다 Stack2로 옮겨줌
                self.stack2.append(self.stack1.pop())
    
        return self.stack2.pop() # Stack2 에서 POP



# Test

q = MyQueue()

q.push(1)
q.push(2)
print(q.pop()) # 1
print(q.pop()) # 2
q.push(3)
print(q.pop()) # 3
q.push(4)
q.push(5)
print(q.pop()) # 4
q.push(6) 
print(q.pop()) # 5
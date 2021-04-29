class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index<0 or index>=self.size or self.head is None:
            return -1
        
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp.val
    
    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        n = Node(val)
        n.next = self.head
        self.head = n
        self.size += 1 

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        n = Node(val)
        temp = self.head
        if temp is None:
            self.head = Node(val)
        else:
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        
        if index<0 or index> self.size:
            return -1
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            n = Node(val)
            temp = self.head
            for i in range(index-1):
                temp = temp.next
            n.next = temp.next
            temp.next = n
            self.size += 1
            
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return

        temp = self.head
        if index == 0:
            self.head = temp.next
            
        else:
            for i in range(index - 1):
                temp = temp.next
            temp.next = temp.next.next
            
        self.size -= 1
        
    #  3) 중간 노드 삭제 :  단방향 연결리스트가 주어졌을 때, 중간(처음과 끝 노드 제외)노드 하나를 삭제하는 알고리즘을 구현하라.
    def deleteNode(self,node):
        if not node or not node.next:
            return -1
        next = node.next
        node.val = next.val 
        node.next = next.next

        self.size -= 1

    # 2)  뒤에서 k번째 원소 구하기:  단방향 연결리스트가 주어졌을 때 뒤에서 k번째 원소를 찾는 알고리즘을 구현하라.
    def findfromback(self,k):
        temp = self.head
        for i in range(self.size-k):
            temp = temp.next
        return temp.val
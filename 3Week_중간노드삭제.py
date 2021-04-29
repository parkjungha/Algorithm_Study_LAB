def deleteNode(node):
    if not node or not node.next:
        return -1
    next = node.next
    node.val = next.val 
    node.next = next.next
    

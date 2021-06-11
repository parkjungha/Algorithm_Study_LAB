class Solution: # Iterative
    def preorderTraversal(self, root: TreeNode) -> List[int]:        
        order = []
        stack = []
        if root== None: 
            return order
        stack.append(root)

        while(len(stack)>0):
            
            node = stack.pop()
            order.append(node.val)

            if node.right != None:
                stack.append(node.right)
            if node.left != None:
                stack.append(node.left)
        return order

class Solution: # Recursive
    def preorderTraversal(self, root: TreeNode) -> List[int]:      
        
        if root is None:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
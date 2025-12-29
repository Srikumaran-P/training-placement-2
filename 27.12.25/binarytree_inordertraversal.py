class Solution(object):
    def inorderTraversal(self, root):
        li=[]
        def inorder(node):
            if not node:
                return None
            inorder(node.left)
            li.append(node.val)
            inorder(node.right)
        inorder(root) 
        return li  
        

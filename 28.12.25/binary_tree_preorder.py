class Solution(object):
    ans = []
    def preorder(self, root):
        #base case
        if root == None:
            return
        #recurive
        self.ans.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        self.ans = []
        self.preorder(root)
        return self.ans

        

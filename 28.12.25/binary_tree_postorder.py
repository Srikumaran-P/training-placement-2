class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        ans = []
        def traversal(root):
            if not root:
                return 
            if not root.left:
                if not root.right:
                    ans.append(root.val)
                else:
                    traversal(root.right)
                    ans.append(root.val)
            else:
                traversal(root.left)
                traversal(root.right)
                ans.append(root.val)
        traversal(root)
        return ans

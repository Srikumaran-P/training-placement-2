class Solution {
    int preIndx = 0;

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        return helper(preorder, inorder, 0, inorder.length - 1);
    }

    public TreeNode helper(int[] preOrder, int[] inOrder, int left, int right) {
        if(left > right){
            return null;
        }
        TreeNode root = new TreeNode(preOrder[preIndx++]);

        int inIndx = Search(inOrder, left, right, root.val);

        root.left = helper(preOrder, inOrder, left, inIndx - 1);
        root.right = helper(preOrder, inOrder, inIndx + 1, right);

        return root;
    }

    public int Search(int[] inOrder, int left, int right, int val) {
        for (int i = left; i <= right; i++) {
            if (inOrder[i] == val) return i;
        }
        return -1;
    }
}

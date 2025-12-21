
class Solution {
    public boolean isSymmetric(TreeNode root) {
        mirror(root.left);
        return isSameTree(root.left,root.right);
    }
    void mirror(TreeNode root) {
        if(root== null) return;
        TreeNode temp = root.left;
        root.left =  root.right;
        root.right = temp;
        mirror(root.left);
        mirror(root.right);
    }

    boolean isSameTree(TreeNode p, TreeNode q) {
        if(p==null && q==null) return true;
        if(p==null || q== null) return false;
        if(p.val!=q.val) return false;
        if(!isSameTree(p.left,q.left) || !isSameTree(p.right,q.right)) return false;
        return true;
    }
}

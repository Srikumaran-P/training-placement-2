class Solution {
    long secondMin = Long.MAX_VALUE;
    int min;

    public int findSecondMinimumValue(TreeNode root) {
        min = root.val;
        dfs(root);
        return secondMin == Long.MAX_VALUE ? -1 : (int) secondMin;
    }

    private void dfs(TreeNode node) {
        if (node == null) return;

        if (node.val > min && node.val < secondMin) {
            secondMin = node.val;
        } 
        else if (node.val == min) {
            dfs(node.left);
            dfs(node.right);
        }
    }
}

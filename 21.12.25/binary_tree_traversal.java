/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        if(root == null) return result;

        Queue<TreeNode> entry = new LinkedList<>();
        entry.add(root);

        while(!entry.isEmpty()){
            List<Integer> level = new ArrayList<>();
            int size = entry.size();

            for(int i = 0; i < size; i++){
            TreeNode curr = entry.poll();
            level.add(curr.val);

                if(curr.left != null) entry.add(curr.left);
                if(curr.right != null) entry.add(curr.right);
            }
            result.add(level);
        }
        return result;
    }

}

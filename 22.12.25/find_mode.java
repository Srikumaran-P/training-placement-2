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
    public int[] findMode(TreeNode root) {
        Queue<Integer> queue = new LinkedList<>();
        Map<Integer,Integer> map = new HashMap<>();
        bst(root,queue);
        while(!queue.isEmpty()) {
            int cur = queue.poll();
            map.put(cur, map.getOrDefault(cur,0) + 1);
        }
        int maxMode = 0;
        for(int value : map.values()) {
            if(maxMode < value) {
                maxMode = value;
            }
        }
        List<Integer> list = new ArrayList<>();
        for(Map.Entry<Integer,Integer> entry : map.entrySet()) {
            if(entry.getValue() == maxMode) {
                list.add(entry.getKey()) ;
            }
        }
        int[] result = new int[list.size()];
        for(int i = 0; i < result.length; i++) {
            result[i] = list.get(i);
        }
        return result;
    }
    public void bst(TreeNode root,  Queue<Integer> queue )
    {
        if(root == null) {
            return ;
        } 
        queue.add(root.val);
        bst(root.left, queue);
        bst(root.right,queue);

    }
    }

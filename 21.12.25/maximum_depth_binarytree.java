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
class node{
    public TreeNode nde;
    public int idx;
    public node(TreeNode nde,int idx){
        this.nde=nde;
        this.idx =idx;
    }
}
class Solution {
    public int widthOfBinaryTree(TreeNode root) {
        Queue<node>q = new LinkedList<>();
        int res = 1;
        q.offer(new node(root,0));
        while(!q.isEmpty()){
            int size = q.size();
            ArrayList<Integer>lst = new ArrayList<>();
            for(int i =0;i<size;i++){
                node curr = q.poll();
                TreeNode node = curr.nde;
                int idx = curr.idx;
                if(node.left!=null){
                    q.offer(new node(node.left,idx*2+1));
                    lst.add(idx*2+1);
                }
                if(node.right!=null){
                    q.offer(new node(node.right,idx*2+2));
                    lst.add(idx*2+2);
                }
            }
            if(lst.size()==0)continue;
            res = Math.max(res,lst.get(lst.size()-1)-lst.get(0)+1);
        }
        return res;
    }
}

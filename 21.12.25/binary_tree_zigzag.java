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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> l=new ArrayList<>();
        if(root==null){return l;}
        Queue<TreeNode> q=new LinkedList<>();
        q.add(root); int pass=0;
        while(!q.isEmpty()){
            int size=q.size();
            List<Integer> lt=new ArrayList<>();
            while(size-->0){
                TreeNode x=q.poll(); if(x!=null){lt.add(x.val);
                
                if(x.left!=null){q.add(x.left);}
                if(x.right!=null){q.add(x.right);}
                }
               

            }
            if(pass%2==0){l.add(lt);}
            else{Collections.reverse(lt);l.add(lt);}
            pass++;

        }

        return l;
        
    }
}

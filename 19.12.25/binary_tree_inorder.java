
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> a;
        inorder(root,a);
        return a;
    }
    void inorder(TreeNode* root,vector<int>& a){
        if(root!=nullptr){
            inorder(root->left,a);
            a.push_back(root->val);
            inorder(root->right,a);
        }
    }
};

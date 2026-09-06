class Solution {
public:
    vector<int> ans;
    int prev = 0;
    int count = 0;
    int maxCount = 0;
    bool first = true;

    void inorder(TreeNode* root) {
        if (root == nullptr)
            return;

        inorder(root->left);

        // Count current value
        if (first || root->val != prev) {
            count = 1;
            first = false;
        } else {
            count++;
        }

        // Update modes
        if (count > maxCount) {
            maxCount = count;
            ans.clear();
            ans.push_back(root->val);
        } 
        else if (count == maxCount) {
            ans.push_back(root->val);
        }

        prev = root->val;

        inorder(root->right);
    }

    vector<int> findMode(TreeNode* root) {
        inorder(root);
        return ans;
    }
};
class Solution {
public:
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<vector<int>> result;
        vector<int> path;
        dfs(root, targetSum, path, result);
        return result;
    }
    void dfs(TreeNode* node, int targetSum, vector<int>& path, vector<vector<int>>& result) {
        if (node == nullptr)
            return;
        path.push_back(node->val);
        targetSum -= node->val;
        if (node->left == nullptr && node->right == nullptr && targetSum == 0) {
            result.push_back(path);
        } else {
            dfs(node->left, targetSum, path, result);
            dfs(node->right, targetSum, path, result);
        }
        path.pop_back();
    }
};
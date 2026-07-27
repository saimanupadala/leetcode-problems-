class Solution {
public:
    string countAndSay(int n) {
        string ans = "1";
        for (int i = 2; i <= n; i++) {
            string temp = "";
            int count = 1;
            for (int j = 0; j < ans.size(); j++) {
                while (j + 1 < ans.size() && ans[j] == ans[j + 1]) {
                    count++;
                    j++;
                }
                temp += to_string(count);
                temp += ans[j];
                count = 1;
            }
            ans = temp;
        }
        return ans;
    }
};
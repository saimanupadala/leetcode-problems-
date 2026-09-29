class Solution {
public:
    vector<string> removeComments(vector<string>& source) {
        vector<string> ans;
        string cur;
        bool block = false;

        for (string line : source) {
            int i = 0;

            while (i < line.size()) {
                if (!block && i + 1 < line.size() && line[i] == '/' && line[i + 1] == '*') {
                    block = true;
                    i += 2;
                }
                else if (block && i + 1 < line.size() && line[i] == '*' && line[i + 1] == '/') {
                    block = false;
                    i += 2;
                }
                else if (!block && i + 1 < line.size() && line[i] == '/' && line[i + 1] == '/') {
                    break;
                }
                else if (!block) {
                    cur += line[i];
                    i++;
                }
                else {
                    i++;
                }
            }

            if (!block && !cur.empty()) {
                ans.push_back(cur);
                cur.clear();
            }
        }

        return ans;
    }
};
bool isMatch(char* s, char* p) {
  int m = strlen(s);
    int n = strlen(p);

    bool dp[m + 1][n + 1];

    // Initialize DP table
    for (int i = 0; i <= m; i++)
        for (int j = 0; j <= n; j++)
            dp[i][j] = false;

    dp[0][0] = true;

    // Handle patterns like a*, a*b*, etc. for empty string
    for (int j = 2; j <= n; j++) {
        if (p[j - 1] == '*')
            dp[0][j] = dp[0][j - 2];
    }
// Fill DP table
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {

            if (p[j - 1] == s[i - 1] || p[j - 1] == '.') {
                dp[i][j] = dp[i - 1][j - 1];
            }
            else if (p[j - 1] == '*') {
                // Zero occurrence of preceding character
                dp[i][j] = dp[i][j - 2];

                // One or more occurrences
                                if (p[j - 2] == s[i - 1] || p[j - 2] == '.') {
                    dp[i][j] = dp[i][j] || dp[i - 1][j];
                }
            }
        }
    }

    return dp[m][n];
}
  

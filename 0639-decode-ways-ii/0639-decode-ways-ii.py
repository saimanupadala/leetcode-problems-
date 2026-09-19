class Solution:
    def numDecodings(self, s):
        MOD = 10**9 + 7

        # dp[i-1] = ways to decode up to previous character
        # dp[i-2] = ways to decode up to character before previous
        prev2 = 1
        prev1 = 9 if s[0] == '*' else (0 if s[0] == '0' else 1)

        for i in range(1, len(s)):
            curr = 0
            a = s[i - 1]
            b = s[i]

            # Decode b as a single character
            if b == '*':
                curr += 9 * prev1
            elif b != '0':
                curr += prev1

            # Decode a and b together
            if a == '*' and b == '*':
                curr += 15 * prev2

            elif a == '*':
                # 11-19 if b is 1-9
                # 10 or 20 if b is 0
                if b == '0':
                    curr += 2 * prev2
                elif b <= '6':
                    curr += 2 * prev2
                else:
                    curr += prev2

            elif b == '*':
                if a == '1':
                    curr += 9 * prev2
                elif a == '2':
                    curr += 6 * prev2

            else:
                num = int(a + b)
                if 10 <= num <= 26:
                    curr += prev2

            curr %= MOD
            prev2, prev1 = prev1, curr

        return prev1
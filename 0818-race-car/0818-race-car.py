class Solution:
    def racecar(self, target: int) -> int:
        dp = {0: 0}

        def get_min_steps(t: int) -> int:
            if t in dp:
                return dp[t]

            # Find k such that 2^(k-1) <= t < 2^k
            k = t.bit_length()
            exact = (1 << k) - 1

            # Case 1: Exact match
            if exact == t:
                dp[t] = k
                return dp[t]

            # Case 2: Overshoot with k 'A's, then reverse
            res = k + 1 + get_min_steps(exact - t)

            # Case 3: Undershoot with (k-1) 'A's, reverse, back up j 'A's, reverse again
            for j in range(k - 1):
                back_dist = (1 << (k - 1)) - (1 << j)
                res = min(res, (k - 1) + 1 + j + 1 + get_min_steps(t - back_dist))

            dp[t] = res
            return res

        return get_min_steps(target)  
class Solution:
    def canCross(self, stones):
   
        dp = {stone: set() for stone in stones}

       
        dp[0].add(0)

        for stone in stones:
            for jump in dp[stone]:

                for next_jump in [jump - 1, jump, jump + 1]:

                    if next_jump > 0:
                        next_stone = stone + next_jump

                        if next_stone in dp:
                            dp[next_stone].add(next_jump)

        return len(dp[stones[-1]]) > 0
        
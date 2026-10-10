
class Solution:
    def numFactoredBinaryTrees(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        arr.sort()
        dp = {}
        
        for x in arr:
            dp[x] = 1
            
            for a in arr:
                if a >= x:
                    break
                
                if x % a == 0:
                    b = x // a
                    
                    if b in dp:
                        dp[x] += dp[a] * dp[b]
                        dp[x] %= MOD
        
        return sum(dp.values()) % MOD

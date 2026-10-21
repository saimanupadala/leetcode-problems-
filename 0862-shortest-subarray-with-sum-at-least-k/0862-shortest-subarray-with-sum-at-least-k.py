from collections import deque
from typing import List

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # Compute prefix sums
        P = [0] * (n + 1)
        for i in range(n):
            P[i + 1] = P[i] + nums[i]
            
        min_length = n + 1
        dq = deque()
        
        for i in range(n + 1):
            # Check if current prefix sum minus the smallest valid prefix sum >= k
            while dq and P[i] - P[dq[0]] >= k:
                min_length = min(min_length, i - dq[0])
                dq.popleft()
                
            # Maintain increasing order of prefix sums in the deque
            while dq and P[i] <= P[dq[-1]]:
                dq.pop()
                
            dq.append(i)
            
        return min_length if min_length <= n else -1
class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        ans = [-1] * n
        stack = []

        for i in range(2 * n):
            current = nums[i % n]

         
            while stack and nums[stack[-1]] < current:
                ans[stack.pop()] = current

          
            if i < n:
                stack.append(i)

        return ans
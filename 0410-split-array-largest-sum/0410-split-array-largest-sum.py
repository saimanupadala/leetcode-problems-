class Solution:
    def splitArray(self, nums, k):

  
        left = max(nums)

        right = sum(nums)

        while left < right:
            mid = (left + right) // 2

            subarrays = 1
            current_sum = 0

            for num in nums:
                if current_sum + num > mid:
                    subarrays += 1
                    current_sum = num
                else:
                    current_sum += num

           
            if subarrays > k:
                left = mid + 1
            else:
                right = mid

        return left
        
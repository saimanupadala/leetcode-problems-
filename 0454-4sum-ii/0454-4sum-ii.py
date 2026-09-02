class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        count = {}

        for a in nums1:
            for b in nums2:
                total = a + b
                count[total] = count.get(total, 0) + 1

        answer = 0

      
        for c in nums3:
            for d in nums4:
                total = c + d

                if -total in count:
                    answer += count[-total]

        return answer
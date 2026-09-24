class Solution:
    def findShortestSubArray(self, nums):
        first = {}
        count = {}
        degree = 0
        answer = len(nums)

        for i, num in enumerate(nums):
            # Store first occurrence
            if num not in first:
                first[num] = i

            # Increase frequency
            count[num] = count.get(num, 0) + 1

            # Update degree
            degree = max(degree, count[num])

        # Find shortest subarray for elements having maximum frequency
        for num in count:
            if count[num] == degree:
                length = first[num]  # start index
                last = 0

                # Find last occurrence
                for i in range(len(nums) - 1, -1, -1):
                    if nums[i] == num:
                        last = i
                        break

                answer = min(answer, last - first[num] + 1)

        return answer
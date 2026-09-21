class Solution:
    def isPossible(self, nums):
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        end = {}

        for num in nums:
            if count[num] == 0:
                continue

            count[num] -= 1

            # Extend an existing subsequence
            if end.get(num - 1, 0) > 0:
                end[num - 1] -= 1
                end[num] = end.get(num, 0) + 1

            # Start a new subsequence: num, num+1, num+2
            elif count.get(num + 1, 0) > 0 and count.get(num + 2, 0) > 0:
                count[num + 1] -= 1
                count[num + 2] -= 1
                end[num + 2] = end.get(num + 2, 0) + 1

            else:
                return False

        return True
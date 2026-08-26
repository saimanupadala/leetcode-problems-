class Solution:
    def maxNumber(self, nums1, nums2, k):

        def max_subsequence(nums, length):
            drop = len(nums) - length
            stack = []

            for num in nums:
                while stack and drop > 0 and stack[-1] < num:
                    stack.pop()
                    drop -= 1

                stack.append(num)

            return stack[:length]

        def merge(a, b):
            result = []

            while a or b:
                if a > b:
                    result.append(a.pop(0))
                else:
                    result.append(b.pop(0))

            return result

        def greater(a, b):
            # Compare two sequences lexicographically
            i = 0

            while i < len(a) and i < len(b):
                if a[i] != b[i]:
                    return a[i] > b[i]
                i += 1

            return len(a) > len(b)

        best = []

        start = max(0, k - len(nums2))
        end = min(k, len(nums1))

        for i in range(start, end + 1):

            part1 = max_subsequence(nums1, i)
            part2 = max_subsequence(nums2, k - i)

            # Merge without destroying original subsequences
            a = part1[:]
            b = part2[:]
            current = []

            while a or b:
                if greater(a, b):
                    current.append(a.pop(0))
                else:
                    current.append(b.pop(0))

            if greater(current, best):
                best = current

        return best
        
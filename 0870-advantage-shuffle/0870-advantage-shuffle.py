
class Solution:
    def advantageCount(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()
        n = len(nums2)

        order = sorted(range(n), key=lambda i: nums2[i])
        result = [0] * n

        left, right = 0, n - 1

        for x in nums1:
            if x > nums2[order[left]]:
                result[order[left]] = x
                left += 1
            else:
                result[order[right]] = x
                right -= 1

        return result

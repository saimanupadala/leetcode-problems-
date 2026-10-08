class Solution:
    def minSwap(self, nums1, nums2):
        n = len(nums1)

        # At index 0
        no_swap = 0
        swap = 1

        for i in range(1, n):

            new_no_swap = float('inf')
            new_swap = float('inf')

            # Case 1: Do not swap at i
            if nums1[i] > nums1[i-1] and nums2[i] > nums2[i-1]:
                new_no_swap = min(new_no_swap, no_swap)
                new_swap = min(new_swap, swap + 1)

            # Case 2: Swap at i
            if nums1[i] > nums2[i-1] and nums2[i] > nums1[i-1]:
                new_no_swap = min(new_no_swap, swap)
                new_swap = min(new_swap, no_swap + 1)

            no_swap = new_no_swap
            swap = new_swap

        return min(no_swap, swap)
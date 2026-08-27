import heapq

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        heap = []
        result = []
        for i in range(min(k, len(nums1))):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

        while heap and len(result) < k:
            total, i, j = heapq.heappop(heap)

            result.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(
                    heap,
                    (nums1[i] + nums2[j + 1], i, j + 1)
                )

        return result
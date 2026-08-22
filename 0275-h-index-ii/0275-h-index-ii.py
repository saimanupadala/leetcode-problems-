class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)

        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) // 2

            # Number of papers from mid to the end
            papers = n - mid

            if citations[mid] >= papers:
                # Possible h-index found, search for a better one
                right = mid - 1
            else:
                # Need more citations
                left = mid + 1

        return n - left
        
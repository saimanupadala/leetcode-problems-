class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)

        h = 0

        for i, citation in enumerate(citations):
            if citation >= i + 1:
                h = i + 1
            else:
                break

        return h
        
class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        groups = set()

        for word in words:
            even = ''.join(sorted(word[0::2]))
            odd = ''.join(sorted(word[1::2]))

            groups.add((even, odd))

        return len(groups)     
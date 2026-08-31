class Solution:
    def findMaximumXOR(self, nums):
        trie = {}

        for num in nums:
            node = trie

            for bit in range(30, -1, -1):
                b = (num >> bit) & 1

                if b not in node:
                    node[b] = {}

                node = node[b]

        ans = 0

        for num in nums:
            node = trie
            curr = 0

            for bit in range(30, -1, -1):
                b = (num >> bit) & 1

                opposite = 1 - b

                if opposite in node:
                    curr |= (1 << bit)
                    node = node[opposite]
                else:
                    node = node[b]

            ans = max(ans, curr)

        return ans
        
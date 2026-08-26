class Solution:
    def maxProduct(self, words):
        masks = []
        lengths = []

        for word in words:
            mask = 0

            for ch in word:
                mask |= 1 << (ord(ch) - ord('a'))

            masks.append(mask)
            lengths.append(len(word))

        answer = 0

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                # No common letters
                if masks[i] & masks[j] == 0:
                    answer = max(answer, lengths[i] * lengths[j])

        return answer
        
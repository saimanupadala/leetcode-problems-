class Solution:
    def palindromePairs(self, words):

        word_map = {word: i for i, word in enumerate(words)}

        result = []

        def is_palindrome(s):
            return s == s[::-1]

        for i, word in enumerate(words):
            length = len(word)

            for j in range(length + 1):
                left = word[:j]
                right = word[j:]

    
                if is_palindrome(left):
                    rev_right = right[::-1]

                    if rev_right in word_map:
                        k = word_map[rev_right]

                        if k != i:
                            result.append([k, i])

            
                if j != length and is_palindrome(right):
                    rev_left = left[::-1]

                    if rev_left in word_map:
                        k = word_map[rev_left]

                        if k != i:
                            result.append([i, k])

        return result
        
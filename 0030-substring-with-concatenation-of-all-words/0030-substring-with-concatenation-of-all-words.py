from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words

        if len(s) < total_len:
            return []

        word_count = Counter(words)
        result = []

        # Try each possible starting offset
        for i in range(word_len):
            left = i
            curr_count = Counter()
            count = 0

            # Move the window in steps of word_len
            for right in range(i, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word in word_count:
                    curr_count[word] += 1
                    count += 1

                    # Shrink the window if a word appears too many times
                    while curr_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        curr_count[left_word] -= 1
                        count -= 1
                        left += word_len

                    # Found a valid window
                    if count == num_words:
                        result.append(left)

                        left_word = s[left:left + word_len]
                        curr_count[left_word] -= 1
                        count -= 1
                        left += word_len

                else:
                    # Reset the window
                    curr_count.clear()
                    count = 0
                    left = right + word_len

        return result
        
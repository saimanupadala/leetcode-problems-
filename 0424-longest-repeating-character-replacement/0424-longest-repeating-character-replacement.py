class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26

        left = 0
        max_freq = 0
        answer = 0

        for right in range(len(s)):
            index = ord(s[right]) - ord('A')
            count[index] += 1

            max_freq = max(max_freq, count[index])

            window_size = right - left + 1
            replacements = window_size - max_freq

       
            if replacements > k:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1

            answer = max(answer, right - left + 1)

        return answer
        
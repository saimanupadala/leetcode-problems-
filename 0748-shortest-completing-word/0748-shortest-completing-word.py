class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        need = {}

        # Count letters in licensePlate
        for ch in licensePlate.lower():
            if ch.isalpha():
                need[ch] = need.get(ch, 0) + 1

        answer = None

        for word in words:
            count = {}

            # Count letters in word
            for ch in word:
                count[ch] = count.get(ch, 0) + 1

            # Check whether word contains all required letters
            valid = True

            for ch in need:
                if count.get(ch, 0) < need[ch]:
                    valid = False
                    break

            if valid:
                if answer is None or len(word) < len(answer):
                    answer = word

        return answer
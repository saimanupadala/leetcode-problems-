class Solution:
    def leastInterval(self, tasks, n):
        freq = [0] * 26

        for task in tasks:
            freq[ord(task) - ord('A')] += 1

        max_freq = max(freq)

        max_count = freq.count(max_freq)

        result = (max_freq - 1) * (n + 1) + max_count

        return max(result, len(tasks))
class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        count1 = 0
        count2 = 0
        index = 0

        # Store previous states to detect a cycle
        seen = {}

        while count1 < n1:
            for ch in s1:
                if ch == s2[index]:
                    index += 1

                    if index == len(s2):
                        index = 0
                        count2 += 1

            count1 += 1

            # If the same index appears again, a cycle exists
            if index in seen:
                prev_count1, prev_count2 = seen[index]

                cycle_s1 = count1 - prev_count1
                cycle_s2 = count2 - prev_count2

                remaining = n1 - count1
                cycles = remaining // cycle_s1

                count1 += cycles * cycle_s1
                count2 += cycles * cycle_s2
            else:
                seen[index] = (count1, count2)

        return count2 // n2
        
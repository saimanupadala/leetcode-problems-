class Solution:
    def magicalString(self, n: int) -> int:
        if n <= 3:
            return 1

        s = [1, 2, 2]

        i = 2
        num = 1
        count = 1

        while len(s) < n:
            # s[i] tells how many times
            # we should add num
            for _ in range(s[i]):
                s.append(num)

                if num == 1 and len(s) <= n:
                    count += 1

            # Change 1 -> 2 or 2 -> 1
            num = 3 - num
            i += 1

        return count
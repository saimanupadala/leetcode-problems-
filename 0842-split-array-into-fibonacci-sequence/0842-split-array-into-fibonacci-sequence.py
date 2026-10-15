
class Solution:
    def splitIntoFibonacci(self, num):
        n = len(num)
        sequence = []
        limit = 2**31 - 1

        def backtrack(index):
            if index == n:
                return len(sequence) >= 3

            value = 0

            for i in range(index, n):
                if i > index and num[index] == '0':
                    break

                value = value * 10 + int(num[i])

                if value > limit:
                    break

                if len(sequence) >= 2:
                    total = sequence[-1] + sequence[-2]

                    if value < total:
                        continue
                    if value > total:
                        break

                sequence.append(value)

                if backtrack(i + 1):
                    return True

                sequence.pop()

            return False

        backtrack(0)
        return sequence
 
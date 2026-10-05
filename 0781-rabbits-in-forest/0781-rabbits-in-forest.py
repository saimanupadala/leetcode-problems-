class Solution:
    def numRabbits(self, answers):
        count = {}
        result = 0

        for x in answers:
            if x not in count or count[x] == 0:
                result += x + 1
                count[x] = x
            else:
                count[x] -= 1

        return result

class Solution:
    def numFriendRequests(self, ages: list[int]) -> int:
        count = [0] * 121

        for age in ages:
            count[age] += 1

        requests = 0

        for age1 in range(1, 121):
            for age2 in range(1, 121):

                if age2 <= 0.5 * age1 + 7:
                    continue

                if age2 > age1:
                    continue

                if age2 > 100 and age1 < 100:
                    continue

                requests += count[age1] * count[age2]

                if age1 == age2:
                    requests -= count[age1]

        return requests

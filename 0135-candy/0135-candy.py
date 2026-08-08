class Solution:
    def candy(self, ratings):
        n = len(ratings)

        # Give every child at least 1 candy
        candies = [1] * n

        # Left to right
        # If current rating is higher than left neighbor,
        # current child gets more candies.
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Right to left
        # If current rating is higher than right neighbor,
        # current child gets more candies.
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)
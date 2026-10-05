class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        INF = float('inf')
        cost = [INF] * n
        cost[src] = 0

        # At most k stops = k + 1 flights
        for _ in range(k + 1):
            temp = cost.copy()

            for u, v, price in flights:
                if cost[u] != INF:
                    temp[v] = min(temp[v], cost[u] + price)

            cost = temp

        if cost[dst] == INF:
            return -1

        return cost[dst]
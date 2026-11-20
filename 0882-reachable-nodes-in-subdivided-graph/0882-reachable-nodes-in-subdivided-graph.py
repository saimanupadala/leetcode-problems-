
import heapq

class Solution:
    def reachableNodes(self, edges, maxMoves, n):
        graph = [[] for _ in range(n)]

        for u, v, cnt in edges:
            graph[u].append((v, cnt + 1))
            graph[v].append((u, cnt + 1))

        dist = [float('inf')] * n
        dist[0] = 0

        pq = [(0, 0)]

        while pq:
            d, u = heapq.heappop(pq)

            if d > dist[u]:
                continue

            for v, w in graph[u]:
                new_dist = d + w

                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))

        ans = sum(d <= maxMoves for d in dist)

        for u, v, cnt in edges:
            a = max(0, maxMoves - dist[u])
            b = max(0, maxMoves - dist[v])

            ans += min(cnt, a + b)

        return ans
  
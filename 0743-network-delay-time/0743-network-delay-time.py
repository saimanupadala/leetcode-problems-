import heapq

class Solution:
    def networkDelayTime(self, times, n, k):
        graph = [[] for _ in range(n + 1)]

        # Build graph
        for u, v, w in times:
            graph[u].append((v, w))

        # Distance from k to every node
        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        # Min heap: (time, node)
        heap = [(0, k)]

        while heap:
            time, node = heapq.heappop(heap)

            # Skip outdated value
            if time > dist[node]:
                continue

            for neighbor, weight in graph[node]:
                new_time = time + weight

                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    heapq.heappush(heap, (new_time, neighbor))

        # If any node is unreachable
        if float('inf') in dist[1:]:
            return -1

        return max(dist[1:])
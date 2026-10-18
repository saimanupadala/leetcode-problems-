from typing import List

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = [[] for _ in range(n)]

        for a, b in richer:
            graph[b].append(a)

        answer = list(range(n))
        visited = [False] * n

        def dfs(person):
            if visited[person]:
                return answer[person]

            visited[person] = True

            for richer_person in graph[person]:
                candidate = dfs(richer_person)

                if quiet[candidate] < quiet[answer[person]]:
                    answer[person] = candidate

            return answer[person]

        for person in range(n):
            dfs(person)

        return answer
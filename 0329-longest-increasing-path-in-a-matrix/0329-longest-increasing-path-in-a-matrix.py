class Solution:
    def longestIncreasingPath(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        
        memo = [[0] * n for _ in range(m)]

        directions = [
            (1, 0),   
            (-1, 0), 
            (0, 1),   
            (0, -1)  
        ]

        def dfs(r, c):
            if memo[r][c] != 0:
                return memo[r][c]

            longest = 1

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (0 <= nr < m and
                    0 <= nc < n and
                    matrix[nr][nc] > matrix[r][c]):

                    longest = max(
                        longest,
                        1 + dfs(nr, nc)
                    )

            memo[r][c] = longest
            return longest

        answer = 0

        for r in range(m):
            for c in range(n):
                answer = max(answer, dfs(r, c))

        return answer
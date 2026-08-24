class Solution:
    def gameOfLife(self, board):
        m = len(board)
        n = len(board[0])

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        for i in range(m):
            for j in range(n):
                live_neighbors = 0

                for di, dj in directions:
                    ni = i + di
                    nj = j + dj

                    if 0 <= ni < m and 0 <= nj < n:
                        # 1 = currently live
                        # 2 = currently live, will die
                        if board[ni][nj] == 1 or board[ni][nj] == 2:
                            live_neighbors += 1
                if board[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = 2   # 1 -> 0
                elif board[i][j] == 0:
                    if live_neighbors == 3:
                        board[i][j] = 3   
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1
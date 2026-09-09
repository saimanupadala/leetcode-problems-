class Solution:
    def updateBoard(self, board, click):
        r, c = click
        m = len(board)
        n = len(board[0])

        # If we clicked on a mine
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board

        def dfs(row, col):
            # Count adjacent mines
            mines = 0

            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr = row + dr
                    nc = col + dc

                    if (0 <= nr < m and
                        0 <= nc < n and
                        board[nr][nc] == 'M'):
                        mines += 1

            # If there are adjacent mines, show the number
            if mines > 0:
                board[row][col] = str(mines)
                return

            # No adjacent mines → blank
            board[row][col] = 'B'

            # Reveal all adjacent unrevealed cells
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr = row + dr
                    nc = col + dc

                    if (0 <= nr < m and
                        0 <= nc < n and
                        board[nr][nc] == 'E'):
                        dfs(nr, nc)

        dfs(r, c)

        return board
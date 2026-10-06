class Solution:
    def validTicTacToe(self, board):
        x_count = sum(row.count('X') for row in board)
        o_count = sum(row.count('O') for row in board)

        # X always starts
        if x_count < o_count or x_count > o_count + 1:
            return False

        def win(player):
            # Rows
            for i in range(3):
                if board[i][0] == player and \
                   board[i][1] == player and \
                   board[i][2] == player:
                    return True

            # Columns
            for j in range(3):
                if board[0][j] == player and \
                   board[1][j] == player and \
                   board[2][j] == player:
                    return True

            # Diagonal
            if board[0][0] == player and \
               board[1][1] == player and \
               board[2][2] == player:
                return True

            if board[0][2] == player and \
               board[1][1] == player and \
               board[2][0] == player:
                return True

            return False

        x_win = win('X')
        o_win = win('O')

        # Both cannot win
        if x_win and o_win:
            return False

        # If X wins, X must have one extra move
        if x_win and x_count != o_count + 1:
            return False

        # If O wins, both counts must be equal
        if o_win and x_count != o_count:
            return False

        return True
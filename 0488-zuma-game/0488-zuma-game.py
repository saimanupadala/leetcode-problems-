from functools import lru_cache
from collections import Counter

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:

        colors = "RYBGW"
        count = Counter(hand)

        # Hand count in fixed order: R, Y, B, G, W
        initial_hand = tuple(count[c] for c in colors)

        # Remove groups of 3 or more
        def shrink(s):
            while True:
                result = []
                i = 0
                changed = False

                while i < len(s):
                    j = i

                    while j < len(s) and s[j] == s[i]:
                        j += 1

                    if j - i >= 3:
                        changed = True
                    else:
                        result.append(s[i:j])

                    i = j

                new_s = ''.join(result)

                if not changed:
                    return new_s

                s = new_s

        @lru_cache(None)
        def dfs(board, hand):

            if not board:
                return 0

            answer = float('inf')

            for c_index in range(5):

                if hand[c_index] == 0:
                    continue

                color = colors[c_index]

                new_hand = list(hand)
                new_hand[c_index] -= 1
                new_hand = tuple(new_hand)

                # Try only useful positions
                for i in range(len(board) + 1):

                    useful = False

                    # Insert next to the same color
                    if i > 0 and board[i - 1] == color:
                        useful = True

                    if i < len(board) and board[i] == color:
                        useful = True

                    # Insert between two equal balls
                    # Example: RR -> RBR
                    if i > 0 and i < len(board):
                        if board[i - 1] == board[i]:
                            useful = True

                    if not useful:
                        continue

                    new_board = board[:i] + color + board[i:]

                    new_board = shrink(new_board)

                    result = dfs(new_board, new_hand)

                    if result != float('inf'):
                        answer = min(answer, 1 + result)

            return answer

        result = dfs(shrink(board), initial_hand)

        return -1 if result == float('inf') else result
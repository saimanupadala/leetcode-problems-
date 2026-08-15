class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board, words):
        # Build Trie
        root = TrieNode()

        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word

        rows = len(board)
        cols = len(board[0])
        result = []

        def dfs(r, c, node):
            char = board[r][c]

            if char not in node.children:
                return

            next_node = node.children[char]

            # Complete word found
            if next_node.word is not None:
                result.append(next_node.word)
                next_node.word = None  # Avoid duplicates

            # Mark cell as visited
            board[r][c] = '#'

            # Up, Down, Left, Right
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (0 <= nr < rows and
                    0 <= nc < cols and
                    board[nr][nc] != '#'):
                    dfs(nr, nc, next_node)

            # Restore cell
            board[r][c] = char

            # Remove unused Trie node
            if not next_node.children and next_node.word is None:
                del node.children[char]

        # Start DFS from every cell
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result
        
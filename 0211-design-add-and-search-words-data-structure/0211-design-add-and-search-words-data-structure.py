class WordDictionary:

    class TrieNode:
        def __init__(self):
            self.children = {}
            self.is_end = False

    def __init__(self):
        self.root = self.TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root

        for ch in word:
            if ch not in current.children:
                current.children[ch] = self.TrieNode()

            current = current.children[ch]

        current.is_end = True

    def search(self, word: str) -> bool:

        def dfs(index, node):
            # Reached the end of the word
            if index == len(word):
                return node.is_end

            ch = word[index]

            # If character is '.',
            # try every possible child
            if ch == '.':
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True

                return False

            # Normal character
            if ch not in node.children:
                return False

            return dfs(index + 1, node.children[ch])

        return dfs(0, self.root)
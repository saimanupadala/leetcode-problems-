class MagicDictionary:

    def __init__(self):
        self.dictionary = []

    def buildDict(self, dictionary):
        self.dictionary = dictionary

    def search(self, searchWord):
        for word in self.dictionary:

            # Length must be the same
            if len(word) != len(searchWord):
                continue

            differences = 0

            for i in range(len(word)):
                if word[i] != searchWord[i]:
                    differences += 1

                # More than one difference is not allowed
                if differences > 1:
                    break

            # Exactly one character must be different
            if differences == 1:
                return True

        return False
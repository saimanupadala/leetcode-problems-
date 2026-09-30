class WordFilter:

    def __init__(self, words):
        self.d = {}

        for index, word in enumerate(words):
            for i in range(len(word) + 1):
                pref = word[:i]

                for j in range(len(word) + 1):
                    suff = word[j:]

                    # Store the latest index
                    self.d[(pref, suff)] = index

    def f(self, pref, suff):
        return self.d.get((pref, suff), -1)
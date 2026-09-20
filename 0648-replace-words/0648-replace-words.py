class Solution:
    def replaceWords(self, dictionary, sentence):
        dictionary.sort(key=len)

        words = sentence.split()

        for i in range(len(words)):
            for root in dictionary:
                if words[i].startswith(root):
                    words[i] = root
                    break

        return " ".join(words)
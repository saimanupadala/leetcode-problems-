
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        result = []

        for word in words:
            map1 = {}
            map2 = {}
            match = True

            for p, w in zip(pattern, word):

                if p in map1 and map1[p] != w:
                    match = False
                    break

                if w in map2 and map2[w] != p:
                    match = False
                    break

                map1[p] = w
                map2[w] = p

            if match:
                result.append(word)

        return result
  

from typing import List

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        replacements = {}

        for i, source, target in zip(indices, sources, targets):
            if s[i:i + len(source)] == source:
                replacements[i] = (source, target)

        result = []
        i = 0

        while i < len(s):
            if i in replacements:
                source, target = replacements[i]
                result.append(target)
                i += len(source)
            else:
                result.append(s[i])
                i += 1

        return ''.join(result)


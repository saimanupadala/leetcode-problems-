
import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        words = re.findall(r'[a-z]+', paragraph.lower())
        banned = set(banned)

        count = Counter(word for word in words if word not in banned)

        return count.most_common(1)[0][0]

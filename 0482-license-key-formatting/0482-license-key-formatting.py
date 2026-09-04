class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:

        # Remove all dashes and convert to uppercase
        s = s.replace("-", "").upper()

        # First group can be shorter
        first = len(s) % k

        result = []

        if first > 0:
            result.append(s[:first])

        # Add remaining groups of size k
        for i in range(first, len(s), k):
            result.append(s[i:i + k])

        return "-".join(result)
class Solution:
    def isValid(self, code: str) -> bool:
        stack = []
        i = 0
        n = len(code)

        while i < n:
            # CDATA
            if code.startswith("<![CDATA[", i):
                if not stack:
                    return False

                end = code.find("]]>", i + 9)

                if end == -1:
                    return False

                i = end + 3

            # End tag
            elif code.startswith("</", i):
                end = code.find(">", i + 2)

                if end == -1:
                    return False

                tag = code[i + 2:end]

                if not (1 <= len(tag) <= 9 and tag.isupper() and tag.isalpha()):
                    return False

                if not stack or stack[-1] != tag:
                    return False

                stack.pop()
                i = end + 1

                # Entire code must be inside one outer tag
                if not stack and i != n:
                    return False

            # Start tag
            elif code[i] == "<":
                end = code.find(">", i + 1)

                if end == -1:
                    return False

                tag = code[i + 1:end]

                if not (1 <= len(tag) <= 9 and tag.isupper() and tag.isalpha()):
                    return False

                stack.append(tag)
                i = end + 1

            # Normal text
            else:
                if not stack:
                    return False

                i += 1

        return len(stack) == 0    
class Solution:
    def deserialize(self, s):
    
        if s[0] != '[':
            return NestedInteger(int(s))

        stack = []
        num = ""
        sign = 1

        for ch in s:
            if ch == '-':
                sign = -1

            elif ch.isdigit():
                num += ch

            elif ch in '[,':
                if ch == '[':
                    stack.append(NestedInteger())
                elif num:
                    stack[-1].add(NestedInteger(sign * int(num)))
                    num = ""
                    sign = 1

            elif ch == ']':
           
                if num:
                    stack[-1].add(NestedInteger(sign * int(num)))
                    num = ""
                    sign = 1

                current = stack.pop()

                if stack:
                    stack[-1].add(current)
                else:
                    return current        
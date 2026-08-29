class Solution:
    def decodeString(self, s):
        stack = []
        current = ""
        number = 0

        for ch in s:

            if ch.isdigit():
                number = number * 10 + int(ch)

            elif ch == '[':
                stack.append((current, number))

                current = ""
                number = 0

            elif ch == ']':
         
                previous, repeat = stack.pop()

                current = previous + current * repeat

            else:
           
                current += ch

        return current
        
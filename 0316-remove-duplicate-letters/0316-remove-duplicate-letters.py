class Solution:
    def removeDuplicateLetters(self, s):
        last = {ch: i for i, ch in enumerate(s)}
        
        stack = []
        seen = set()

        for i, ch in enumerate(s):
            if ch in seen:
                continue

            
            while stack and stack[-1] > ch and last[stack[-1]] > i:
                removed = stack.pop()
                seen.remove(removed)

            stack.append(ch)
            seen.add(ch)

        return ''.join(stack)
        
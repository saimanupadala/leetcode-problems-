class NestedIterator:
    def __init__(self, nestedList):
        self.stack = nestedList[::-1]

    def next(self):
        self.hasNext()
        return self.stack.pop().getInteger()

    def hasNext(self):
        while self.stack:
            top = self.stack[-1]

            if top.isInteger():
                return True


            self.stack.pop()
            for item in reversed(top.getList()):
                self.stack.append(item)

        return False

         
class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.index = 0

    def next(self, n: int) -> int:
        while self.index < len(self.encoding):
            if self.encoding[self.index] >= n:
                self.encoding[self.index] -= n
                return self.encoding[self.index + 1]

            n -= self.encoding[self.index]
            self.index += 2

        return -1
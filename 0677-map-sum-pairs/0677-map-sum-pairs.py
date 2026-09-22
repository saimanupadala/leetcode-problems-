class MapSum:

    def __init__(self):
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        self.map[key] = val

    def sum(self, prefix: str) -> int:
        total = 0

        for key in self.map:
            if key.startswith(prefix):
                total += self.map[key]

        return total
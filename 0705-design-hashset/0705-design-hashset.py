class MyHashSet:

    def __init__(self):
        self.set = [False] * 1000001

    def add(self, key):
        self.set[key] = True

    def remove(self, key):
        self.set[key] = False

    def contains(self, key):
        return self.set[key]
class MyHashMap:

    def __init__(self):
        self.data = [-1] * 1000001

    def put(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data[key]

    def remove(self, key):
        self.data[key] = -1
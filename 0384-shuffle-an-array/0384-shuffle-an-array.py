import random

class Solution:

    def __init__(self, nums):
        self.original = nums[:]

    def reset(self):
        return self.original[:]

    def shuffle(self):
        arr = self.original[:]

        for i in range(len(arr) - 1, 0, -1):
            j = random.randint(0, i)

            arr[i], arr[j] = arr[j], arr[i]

        return arr
class NumArray:

    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (2 * self.n)

        # Store elements in the second half
        for i in range(self.n):
            self.tree[self.n + i] = nums[i]

        # Build the segment tree
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index, val):
        # Move to the leaf
        index += self.n
        self.tree[index] = val

        # Update all affected parents
        index //= 2

        while index:
            self.tree[index] = self.tree[2 * index] + self.tree[2 * index + 1]
            index //= 2

    def sumRange(self, left, right):
        left += self.n
        right += self.n

        total = 0

        while left <= right:
            if left % 2 == 1:
                total += self.tree[left]
                left += 1

            if right % 2 == 0:
                total += self.tree[right]
                right -= 1

            left //= 2
            right //= 2

        return total
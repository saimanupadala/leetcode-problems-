class RangeModule:

    def __init__(self):
        self.ranges = []

    def addRange(self, left, right):
        new_ranges = []
        i = 0

        while i < len(self.ranges) and self.ranges[i][1] < left:
            new_ranges.append(self.ranges[i])
            i += 1

        while i < len(self.ranges) and self.ranges[i][0] <= right:
            left = min(left, self.ranges[i][0])
            right = max(right, self.ranges[i][1])
            i += 1

        new_ranges.append([left, right])

        while i < len(self.ranges):
            new_ranges.append(self.ranges[i])
            i += 1

        self.ranges = new_ranges

    def queryRange(self, left, right):
        for l, r in self.ranges:
            if l > left:
                break

            if l <= left and right <= r:
                return True

        return False

    def removeRange(self, left, right):
        new_ranges = []

        for l, r in self.ranges:

            # Completely before or after the removed range
            if r <= left or l >= right:
                new_ranges.append([l, r])

            else:
                # Keep left part
                if l < left:
                    new_ranges.append([l, left])

                # Keep right part
                if r > right:
                    new_ranges.append([right, r])

        self.ranges = new_ranges
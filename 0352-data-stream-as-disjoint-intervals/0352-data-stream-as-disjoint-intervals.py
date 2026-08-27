class SummaryRanges:

    def __init__(self):
        self.nums = set()

    def addNum(self, value: int) -> None:
        self.nums.add(value)

    def getIntervals(self):
        nums = sorted(self.nums)
        result = []

        if not nums:
            return result

        start = nums[0]
        end = nums[0]

        for num in nums[1:]:
            if num == end + 1:
                end = num
            else:
                result.append([start, end])
                start = num
                end = num
        result.append([start, end])

        return result
class MyCalendarThree:

    def __init__(self):
        self.time = {}

    def book(self, startTime: int, endTime: int) -> int:
        self.time[startTime] = self.time.get(startTime, 0) + 1
        self.time[endTime] = self.time.get(endTime, 0) - 1

        active = 0
        answer = 0

        for t in sorted(self.time):
            active += self.time[t]
            answer = max(answer, active)

        return answer
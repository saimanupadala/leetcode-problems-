class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, startTime: int, endTime: int) -> bool:
        for start, end in self.events:
            # Check if the new event overlaps
            if startTime < end and endTime > start:
                return False

        # No overlap, so add the event
        self.events.append((startTime, endTime))
        return True
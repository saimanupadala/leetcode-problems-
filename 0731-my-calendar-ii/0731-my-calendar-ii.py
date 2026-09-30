class MyCalendarTwo:

    def __init__(self):
        self.events = []
        self.overlaps = []

    def book(self, startTime: int, endTime: int) -> bool:

        # Check if this booking creates a triple booking
        for start, end in self.overlaps:
            if startTime < end and endTime > start:
                return False

        # Find new double-booked parts
        for start, end in self.events:
            if startTime < end and endTime > start:
                overlap_start = max(startTime, start)
                overlap_end = min(endTime, end)

                self.overlaps.append((overlap_start, overlap_end))

        # Add the new event
        self.events.append((startTime, endTime))

        return True
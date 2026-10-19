
class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.students = []

    def seat(self) -> int:
        if not self.students:
            self.students.append(0)
            return 0

        max_dist = self.students[0]
        seat_pos = 0

        for i in range(1, len(self.students)):
            prev = self.students[i - 1]
            curr = self.students[i]
            dist = (curr - prev) // 2

            if dist > max_dist:
                max_dist = dist
                seat_pos = prev + dist

        last_dist = self.n - 1 - self.students[-1]

        if last_dist > max_dist:
            seat_pos = self.n - 1

        self.students.append(seat_pos)
        self.students.sort()

        return seat_pos

    def leave(self, p: int) -> None:
        self.students.remove(p)

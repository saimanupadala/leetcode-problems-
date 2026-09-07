class Solution:
    def findMinMoves(self, machines):
        n = len(machines)
        total = sum(machines)

        # Impossible to distribute equally
        if total % n != 0:
            return -1

        avg = total // n
        moves = 0
        balance = 0

        for dresses in machines:
            balance += dresses - avg

            # Maximum dresses crossing a boundary
            moves = max(moves, abs(balance))

            # Dresses this machine needs to send
            moves = max(moves, dresses - avg)

        return moves
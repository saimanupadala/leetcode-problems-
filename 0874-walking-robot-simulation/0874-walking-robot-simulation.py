
class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        obstacle_set = {(x, y) for x, y in obstacles}

        x, y = 0, 0
        direction = 0
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        max_dist = 0

        for command in commands:
            if command == -2:
                direction = (direction + 3) % 4
            elif command == -1:
                direction = (direction + 1) % 4
            else:
                for _ in range(command):
                    nx = x + dx[direction]
                    ny = y + dy[direction]

                    if (nx, ny) in obstacle_set:
                        break

                    x, y = nx, ny
                    max_dist = max(max_dist, x * x + y * y)

        return max_dist
     
class Solution:
    def escapeGhosts(self, ghosts, target):
        # Pac-Man's distance from (0, 0) to target
        my_distance = abs(target[0]) + abs(target[1])

        for ghost in ghosts:
            # Ghost's distance to target
            ghost_distance = abs(ghost[0] - target[0]) + abs(ghost[1] - target[1])

            # Ghost can reach target at the same time or earlier
            if ghost_distance <= my_distance:
                return False

        return True
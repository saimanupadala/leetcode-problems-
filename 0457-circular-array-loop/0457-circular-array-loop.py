class Solution:
    def circularArrayLoop(self, nums: list[int]) -> bool:
        n = len(nums)

        for i in range(n):
            if nums[i] == 0:
                continue

            direction = nums[i] > 0
            current = i
            path = []

            while True:
                # Wrong direction or already processed
                if nums[current] == 0:
                    break

                if (nums[current] > 0) != direction:
                    break

                # Self-loop is not allowed
                next_index = (current + nums[current]) % n

                if next_index == current:
                    break

                # Cycle found
                if current in path:
                    return True

                path.append(current)
                current = next_index

            # Mark all visited nodes as processed
            for index in path:
                nums[index] = 0

        return False
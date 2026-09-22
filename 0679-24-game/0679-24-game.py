class Solution:
    def judgePoint24(self, cards):
        nums = [float(x) for x in cards]

        def solve(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6

            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):

                    # Numbers not selected
                    remaining = [
                        nums[k] for k in range(len(nums))
                        if k != i and k != j
                    ]

                    a = nums[i]
                    b = nums[j]

                    # All possible results
                    results = [
                        a + b,
                        a - b,
                        b - a,
                        a * b
                    ]

                    if abs(b) > 1e-6:
                        results.append(a / b)

                    if abs(a) > 1e-6:
                        results.append(b / a)

                    for value in results:
                        remaining.append(value)

                        if solve(remaining):
                            return True

                        remaining.pop()

            return False

        return solve(nums)
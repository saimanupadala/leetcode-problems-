class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []

        def backtrack(index, expression, value, prev):
            if index == len(num):
                if value == target:
                    result.append(expression)
                return

            for i in range(index, len(num)):
                # Don't allow numbers with leading zeros
                if i > index and num[index] == '0':
                    break

                current = num[index:i + 1]
                curr_num = int(current)

                if index == 0:
                    # First number
                    backtrack(
                        i + 1,
                        current,
                        curr_num,
                        curr_num
                    )
                else:
                    # Addition
                    backtrack(
                        i + 1,
                        expression + "+" + current,
                        value + curr_num,
                        curr_num
                    )

                    # Subtraction
                    backtrack(
                        i + 1,
                        expression + "-" + current,
                        value - curr_num,
                        -curr_num
                    )

                    # Multiplication
                    backtrack(
                        i + 1,
                        expression + "*" + current,
                        value - prev + prev * curr_num,
                        prev * curr_num
                    )

        backtrack(0, "", 0, 0)
        return result
        
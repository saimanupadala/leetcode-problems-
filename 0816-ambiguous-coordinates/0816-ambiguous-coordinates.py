class Solution:
    def ambiguousCoordinates(self, s: str) -> list[str]:
        # Strip outer parentheses
        digits = s[1:-1]
        n = len(digits)
        res = []

        def get_valid_numbers(num_str: str) -> list[str]:
            """Generates all valid integer and decimal representations of num_str."""
            valid = []
            m = len(num_str)

            # Option 1: No decimal point (as an integer)
            # Valid if single digit or doesn't start with '0'
            if m == 1 or not num_str.startswith('0'):
                valid.append(num_str)

            # Option 2: Inserting a decimal point at position d (1 <= d < m)
            for d in range(1, m):
                left, right = num_str[:d], num_str[d:]

                # Left part valid: '0' alone OR doesn't start with '0'
                # Right part valid: doesn't end with '0'
                if (left == "0" or not left.startswith('0')) and not right.endswith('0'):
                    valid.append(left + "." + right)

            return valid

        # Split digits into x and y parts
        for i in range(1, n):
            x_parts = get_valid_numbers(digits[:i])
            y_parts = get_valid_numbers(digits[i:])

            # Combine all valid x and y pairs
            for x_val in x_parts:
                for y_val in y_parts:
                    res.append(f"({x_val}, {y_val})")

        return res
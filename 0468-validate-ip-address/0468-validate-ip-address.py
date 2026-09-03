class Solution:
    def validIPAddress(self, queryIP: str) -> str:

        # Check IPv4
        if "." in queryIP:
            parts = queryIP.split(".")

            if len(parts) != 4:
                return "Neither"

            for part in parts:
                # Empty part
                if not part:
                    return "Neither"

                # Only digits
                if not part.isdigit():
                    return "Neither"

                # Leading zero
                if len(part) > 1 and part[0] == '0':
                    return "Neither"

                # Value must be 0 to 255
                if int(part) > 255:
                    return "Neither"

            return "IPv4"

        # Check IPv6
        elif ":" in queryIP:
            parts = queryIP.split(":")

            if len(parts) != 8:
                return "Neither"

            hex_chars = "0123456789abcdefABCDEF"

            for part in parts:
                if not (1 <= len(part) <= 4):
                    return "Neither"

                for ch in part:
                    if ch not in hex_chars:
                        return "Neither"

            return "IPv6"

        return "Neither"
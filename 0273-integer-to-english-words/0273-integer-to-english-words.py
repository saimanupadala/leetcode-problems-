class Solution:
    def numberToWords(self, num: int) -> str:

        if num == 0:
            return "Zero"

        below_20 = [
            "", "One", "Two", "Three", "Four", "Five",
            "Six", "Seven", "Eight", "Nine", "Ten",
            "Eleven", "Twelve", "Thirteen", "Fourteen",
            "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"
        ]

        tens = [
            "", "", "Twenty", "Thirty", "Forty",
            "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
        ]

        def convert(n):
            if n < 20:
                return below_20[n]

            if n < 100:
                return tens[n // 10] + (" " + below_20[n % 10] if n % 10 else "")

            return (
                below_20[n // 100] + " Hundred" +
                (" " + convert(n % 100) if n % 100 else "")
            )

        result = []

        if num >= 1_000_000_000:
            result.append(convert(num // 1_000_000_000))
            result.append("Billion")
            num %= 1_000_000_000

        if num >= 1_000_000:
            result.append(convert(num // 1_000_000))
            result.append("Million")
            num %= 1_000_000

        if num >= 1000:
            result.append(convert(num // 1000))
            result.append("Thousand")
            num %= 1000

        if num > 0:
            result.append(convert(num))

        return " ".join(result)
        
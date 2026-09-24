class Solution:
    def minStickers(self, stickers, target):
        n = len(target)
        full = (1 << n) - 1

        # Convert stickers to character counts
        sticker_counts = []

        for sticker in stickers:
            count = [0] * 26
            for ch in sticker:
                count[ord(ch) - ord('a')] += 1
            sticker_counts.append(count)

        # dp[mask] = minimum stickers needed
        # to form the characters represented by mask
        dp = [float('inf')] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):
            if dp[mask] == float('inf'):
                continue

            for count in sticker_counts:
                new_mask = mask
                used = count[:]

                # Try to use this sticker for missing characters
                for i in range(n):
                    if (new_mask >> i) & 1 == 0:
                        ch = ord(target[i]) - ord('a')

                        if used[ch] > 0:
                            used[ch] -= 1
                            new_mask |= (1 << i)

                dp[new_mask] = min(dp[new_mask], dp[mask] + 1)

        if dp[full] == float('inf'):
            return -1

        return dp[full]
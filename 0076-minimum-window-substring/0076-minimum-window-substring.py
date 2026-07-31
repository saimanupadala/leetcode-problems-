class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1
        window = {}
        required = len(need)
        formed = 0
        left = 0
        min_len = float('inf')
        start = 0
        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1
            if ch in need and window[ch] == need[ch]:
                formed += 1
            while left <= right and formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left
                left_char = s[left]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1
                left += 1
        return "" if min_len == float('inf') else s[start:start + min_len]
        
class Solution:
    def primePalindrome(self, n: int) -> int:
        if n <= 2:
            return 2
        if n <= 3:
            return 3
        if n <= 5:
            return 5
        if n <= 7:
            return 7
        if n <= 11:
            return 11
            
        def is_prime(num: int) -> bool:
            if num < 2:
                return False
            if num in (2, 3):
                return True
            if num % 2 == 0 or num % 3 == 0:
                return False
            i = 5
            while i * i <= num:
                if num % i == 0 or num % (i + 2) == 0:
                    return False
                i += 6
            return True

        s = str(n)
        L = len(s)
        
        # All even-length palindromes greater than 11 are divisible by 11,
        # so they cannot be prime. If n has an even length and > 11,
        # the next possible prime palindrome must have an odd length.
        if L % 2 == 0:
            n = 10 ** L
            s = str(n)
            L = len(s)
            
        while True:
            k = (L + 1) // 2
            start_root = int(s[:k])
            max_root = 10 ** k
            
            for root in range(start_root, max_root):
                s_root = str(root)
                pal_str = s_root + s_root[:-1][::-1]
                pal = int(pal_str)
                if pal >= n and is_prime(pal):
                    return pal
            
            L += 2
            n = 10 ** (L - 1)
            s = str(n)
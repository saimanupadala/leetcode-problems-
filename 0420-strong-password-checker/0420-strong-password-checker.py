class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)

    
        lower = any(c.islower() for c in password)
        upper = any(c.isupper() for c in password)
        digit = any(c.isdigit() for c in password)

        missing = 0
        if not lower:
            missing += 1
        if not upper:
            missing += 1
        if not digit:
            missing += 1

     
        runs = []
        i = 0

        while i < n:
            j = i

            while j < n and password[j] == password[i]:
                j += 1

            length = j - i

            if length >= 3:
                runs.append(length)

            i = j

      
        if n < 6:
            return max(missing, 6 - n)

        if n <= 20:
            replace = sum(length // 3 for length in runs)
            return max(missing, replace)

        delete = n - 20

        replace = sum(length // 3 for length in runs)

        for i in range(len(runs)):
            if delete <= 0:
                break

            if runs[i] % 3 == 0:
                runs[i] -= 1
                delete -= 1
                replace -= 1

        for i in range(len(runs)):
            if delete <= 0:
                break

            if runs[i] % 3 == 1:
                d = min(delete, 2)
                runs[i] -= d
                delete -= d

                if d == 2:
                    replace -= 1

        for i in range(len(runs)):
            if delete <= 0:
                break

            d = min(delete, (runs[i] // 3) * 3)

            runs[i] -= d
            delete -= d
            replace -= d // 3

 
        return (n - 20) + max(missing, replace)
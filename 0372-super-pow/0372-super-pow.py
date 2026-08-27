class Solution:
    def superPow(self, a, b):
        MOD = 1337

        def pow_mod(a, n):
            result = 1

            while n > 0:
                if n % 2 == 1:
                    result = (result * a) % MOD

                a = (a * a) % MOD
                n //= 2

            return result

        result = 1
        a %= MOD

        for digit in b:
            result = (pow_mod(result, 10) * pow_mod(a, digit)) % MOD

        return result
        
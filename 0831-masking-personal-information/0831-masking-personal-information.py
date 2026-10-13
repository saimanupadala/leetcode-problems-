
class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            name, domain = s.split('@')
            return name[0].lower() + '*****' + name[-1].lower() + '@' + domain.lower()

        digits = ''.join(c for c in s if c.isdigit())
        local = '***-***-' + digits[-4:]

        country = len(digits) - 10
        if country > 0:
            return '+' + '*' * country + '-' + local

        return local

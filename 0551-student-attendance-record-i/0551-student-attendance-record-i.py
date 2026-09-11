class Solution:
    def checkRecord(self, s):
        # More than 1 absence
        if s.count('A') >= 2:
            return False

        # 3 consecutive late days
        if 'LLL' in s:
            return False

        return True
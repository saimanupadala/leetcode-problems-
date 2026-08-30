class Solution:
    def addStrings(self, num1, num2):

        i = len(num1) - 1
        j = len(num2) - 1

        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:

        
            if i >= 0:
                digit1 = ord(num1[i]) - ord('0')
                i -= 1
            else:
                digit1 = 0

     
            if j >= 0:
                digit2 = ord(num2[j]) - ord('0')
                j -= 1
            else:
                digit2 = 0

        
            total = digit1 + digit2 + carry

            result.append(str(total % 10))
            carry = total // 10

     
        return ''.join(result[::-1])
        
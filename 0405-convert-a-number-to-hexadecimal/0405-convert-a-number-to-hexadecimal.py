class Solution:
    def toHex(self, num):

        if num == 0:
            return "0"

       
        if num < 0:
            num += 2 ** 32

        hex_chars = "0123456789abcdef"
        result = ""

        while num > 0:
            digit = num & 15   
            result = hex_chars[digit] + result
            num >>= 4            

        return result
        
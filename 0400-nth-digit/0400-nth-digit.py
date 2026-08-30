class Solution:
    def findNthDigit(self, n):
     
        digits = 1
        start = 1
        count = 9

        while n > digits * count:
            n -= digits * count
            digits += 1
            start *= 10
            count *= 10

   
        number = start + (n - 1) // digits


        index = (n - 1) % digits

        return int(str(number)[index])
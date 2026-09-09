class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        
        # Split the complex numbers
        a, b = num1[:-1].split('+')
        c, d = num2[:-1].split('+')
        
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        
        # (a + bi)(c + di)
        real = a * c - b * d
        imaginary = a * d + b * c
        
        return str(real) + "+" + str(imaginary) + "i"
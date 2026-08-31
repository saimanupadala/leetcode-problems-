class Solution:
    def originalDigits(self, s: str) -> str:
        count = [0] * 26

     
        for c in s:
            count[ord(c) - ord('a')] += 1

        digits = [0] * 10

       
        digits[0] = count[ord('z') - ord('a')]      
        digits[2] = count[ord('w') - ord('a')]       
        digits[4] = count[ord('u') - ord('a')]       
        digits[6] = count[ord('x') - ord('a')]       
        digits[8] = count[ord('g') - ord('a')]       

        digits[3] = count[ord('h') - ord('a')] - digits[8]   
        digits[5] = count[ord('f') - ord('a')] - digits[4]   
        digits[7] = count[ord('s') - ord('a')] - digits[6]   

        digits[1] = count[ord('o') - ord('a')] - digits[0] - digits[2] - digits[4]

        digits[9] = count[ord('i') - ord('a')] - digits[5] - digits[6] - digits[8]

        result = ""

        for i in range(10):
            result += str(i) * digits[i]

        return result
        
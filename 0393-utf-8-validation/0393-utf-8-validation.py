class Solution:
    def validUtf8(self, data):
        remaining = 0

        for num in data:
           
            num = num & 255

            if remaining == 0:
             
                if (num >> 7) == 0:
                    remaining = 0

              
                elif (num >> 5) == 0b110:
                    remaining = 1

             
                elif (num >> 4) == 0b1110:
                    remaining = 2

              
                elif (num >> 3) == 0b11110:
                    remaining = 3

                else:
                    return False

            else:
           
                if (num >> 6) != 0b10:
                    return False

                remaining -= 1

        return remaining == 0
        
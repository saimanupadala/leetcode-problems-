import math

class Solution:
    def canMeasureWater(self, x, y, target):
      
        if target > x + y:
            return False

        if target == 0:
            return True

     
        return target % math.gcd(x, y) == 0
        
# The guess API is already defined.
# @param num, your guess
# @return -1 if num is higher than pick
#          1 if num is lower than pick
#          0 if num is equal to pick

class Solution:
    def guessNumber(self, n):
        left = 1
        right = n

        while left <= right:
            mid = left + (right - left) // 2

            result = guess(mid)

            if result == 0:
                return mid

            elif result == -1:
    
                right = mid - 1

            else:
                left = mid + 1
        
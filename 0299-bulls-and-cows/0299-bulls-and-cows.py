class Solution:
    def getHint(self, secret, guess):
        bulls = 0
        secret_count = [0] * 10
        guess_count = [0] * 10

        # Find bulls
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                secret_count[int(secret[i])] += 1
                guess_count[int(guess[i])] += 1
        cows = 0
        for i in range(10):
            cows += min(secret_count[i], guess_count[i])

        return str(bulls) + "A" + str(cows) + "B"
        
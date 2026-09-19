class Solution:
    def shoppingOffers(self, price, special, needs):
        n = len(price)
        memo = {}

        def dfs(needs):
            # If already calculated
            if tuple(needs) in memo:
                return memo[tuple(needs)]

            # Option 1: Buy everything normally
            cost = 0
            for i in range(n):
                cost += needs[i] * price[i]

            # Option 2: Try every special offer
            for offer in special:
                new_needs = []
                valid = True

                for i in range(n):
                    if offer[i] > needs[i]:
                        valid = False
                        break
                    new_needs.append(needs[i] - offer[i])

                # Offer can be used
                if valid:
                    cost = min(
                        cost,
                        offer[n] + dfs(new_needs)
                    )

            memo[tuple(needs)] = cost
            return cost

        return dfs(needs)   
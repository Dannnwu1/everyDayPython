from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {0: 0}
        coins.sort()

        def min_coins(amt):
            if amt in memo:
                return memo[amt]
            min_coin = float("inf")
            for coin in coins:
                diff = amt - coin
                if diff < 0:
                    break
                min_coin = min(min_coin, 1 + min_coins(diff))
                memo[amt] = min_coin
            return min_coin

        result = min_coins(amount)
        return result if result < float("inf") else -1

    def coinChange_tb(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        coins.sort()

        for i in range(1, amount + 1):
            min_coin = float("inf")
            for coin in coins:
                diff = i - coin
                if diff < 0:
                    break
                min_coin = min(min_coin, 1 + dp[diff])
                dp[i] = min_coin

        return dp[amount] if dp[amount] < float("inf") else -1


if __name__ == "__main__":
    so = Solution()
    coins = [1, 2, 5]
    amount = 11
    print(so.coinChange(coins, amount))

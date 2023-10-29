from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [9876543210] * (amount+1)
        dp[0] = 0
        coins = sorted(coins)

        for c in coins:
            if c >= amount+1: continue
            dp[c] = 1

        for i in range(amount+1):
            for coin in coins:
                if i+coin >= amount+1:
                    break
                dp[i+coin] = min(dp[i+coin], dp[i] + 1)

        if dp[-1] == 9876543210:
            return -1
        else:
            return dp[-1]










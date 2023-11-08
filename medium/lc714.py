from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        own = [0]*n
        not_own = [0]*n

        own[0] = -prices[0] - fee

        for i in range(1, n):
            own[i] = max(own[i-1], not_own[i-1] - prices[i] - fee )
            not_own[i] = max(not_own[i-1], own[i-1] + prices[i])

        return max(own[-1], not_own[-1])
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        mv = 999999999
        for n in prices:
            mv = min(n, mv)
            result = max(result, n - mv)

        return result
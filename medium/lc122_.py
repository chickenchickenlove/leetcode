from typing import List

def sol(i, n, p):
    if i == 0:
        return 0
    # Top - Bottom DP.
    # d(3) = max(d(2), d(2) + (2,3), (0,3))
    pre_v = sol(i-1, n, p)
    diff = p[i]-p[i-1]
    start_diff = p[i]-p[0]
    return max(pre_v + diff, pre_v, start_diff)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1: return 0
        return sol(n-1, n, prices)


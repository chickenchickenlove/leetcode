from typing import List

class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        house = len(costs)
        color = len(costs[0])
        dp = [[0]*color for _ in range(house)]
        for i in range(color):
            dp[0][i] = costs[0][i]

        for i in range(1, house):
            for j in range(color):
                min_v = 9876543210
                for k in range(color):
                    if j == k : continue
                    min_v = min(dp[i-1][k], min_v)
                dp[i][j] = min_v + costs[i][j]
        return min(dp[house-1])


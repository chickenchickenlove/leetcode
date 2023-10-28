class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n >= 3 and k == 1:
            return 0

        dp = [0 for _ in range(n+1)]
        dp[1] = 1

        if n >= 2:
            dp[2] = dp[1] * k

        for i in range(3, n+1):
            if i == 3:
                dp[i] = dp[i-1]*k - 1
                continue
            dp[i] = dp[i-1]*k - (dp[i-3]*(k-1))

        return dp[-1]*k



class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]

        # init value
        dp[0] = 1
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n+1):
            for diff in range(1, i):
                j = i-diff
                dp[i] = max(j*diff, dp[j]*diff, dp[j]*dp[diff], j*dp[diff], dp[i])

        return dp[-1]

Solution().integerBreak(10)










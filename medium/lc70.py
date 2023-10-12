class Solution:
    def jump(self, nums: List[int]) -> int:
        MAX = 99999
        dp = [MAX for _ in range(len(nums))]
        dp[0] = 0

        for i, n in enumerate(nums):
            max_jump = min(i + n, len(nums) - 1)
            for r in range(i, max_jump + 1):
                if dp[r] > dp[i]:
                    dp[r] = dp[i] + 1
        return dp[-1]
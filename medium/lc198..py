from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * 2 for _ in range(n)]

        # 1 : 훔침, 0: 안 훔침
        dp[0][1] = nums[0]
        ret = nums[0]
        if n > 1:
            dp[1][0] = nums[0]
            dp[1][1] = nums[1]
            ret = max(ret, nums[1])


        for day in range(2, n):
            dp[day][0] = max(dp[day-1][1], dp[day-1][0])
            dp[day][1] = dp[day-1][0] + nums[day]

            ret = max(ret, dp[day][0], dp[day][1])

        return ret


Solution().rob([100,1,1,100])
Solution().rob([0])
Solution().rob([0])
# Solution().rob([1,2,3,1])
# Solution().rob([2,1])





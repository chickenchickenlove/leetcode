from typing import List

# 하나로 관리하는 경우 다음 문제가 발생함.
# 0번에서 샀는지를 True로 관리할 수가 있음. 그런데 이렇게 할 경우, 1번에서 사는 가격보다 0번에서 훔친 가격이 더 큰 경우 1번은 항상 True로 됨.
# 그런데 1번이 항상 True인 경우에, 마지막이 가장 큰 숫자가 있을 경우가 있음. 이럴 때는 1번을 빼야하는데, 1번을 빼면 2번을 살 수 있는데 안 산 경우가 됨.

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # 0번은 무조건 사는 곳
        dp = [[0]*2 for _ in range(n)]
        # 0번은 무조건 안 사는 곳
        dpn = [[0]*2 for _ in range(n)]

        # 1 : 훔침, 0: 안 훔침
        dp[0][1] = nums[0]
        ret = nums[0]
        if n > 1:
            dp[1][0] = nums[0]
            dp[1][1] = nums[1]
            dpn[1][1] = nums[1]
            ret = max(ret, dp[1][0], dp[1][1], dpn[1][1])

        for day in range(2, n):

            if n-1 == day:
                dp[day][1] = dp[day-1][0]
            else:
                dp[day][1] = dp[day - 1][0] + nums[day]
            dp[day][0] = max(dp[day-1][1], dp[day-1][0])

            dpn[day][0] = max(dpn[day-1][1], dpn[day-1][0])
            dpn[day][1] = dpn[day - 1][0] + nums[day]

            ret = max(*dp[day], *dpn[day], ret)

        return ret


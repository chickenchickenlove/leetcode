from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        d = [0 for _ in range(len(nums))]
        d[0] = nums[0]
        if len(nums) == 1:
            return d[0]

        result = d[0]
        for i in range(1, len(nums)):
            d[i] = max(d[i-1] + nums[i], nums[i])
            result = max(result , d[i])

        return result


print(Solution().maxSubArray([-1,-2]))


# d[i] = max(d[i-1] + p[i], p[i])

# 띄어넘는 것이 가능한지
# 선택하지 않으면 0이 맞는지? -> 아니다. p[i]임


# // 0, 1, 0, 4, 3, 5, 6,
# // 0, 1, 0, 4, 3, 5, 6, 1, 5
#
#
#
#
#
# // 5, 9, 8, 15, 23
# // 9, -1, 0  = 8
# // max
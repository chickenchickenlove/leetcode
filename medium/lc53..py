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



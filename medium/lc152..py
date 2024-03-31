from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        # negative한 경우 기억하고, 다시 곱하면 됨.
        # plus이면 곱해도 계속 커짐.
        Max = Min = result = 0
        for i in range(n):
            current = nums[i]
            temp_max = max(current, Max * current, Min * current)
            Min = min(current, Min * current, Max * current)

            result = max(temp_max, result)
            Max = temp_max

        return result
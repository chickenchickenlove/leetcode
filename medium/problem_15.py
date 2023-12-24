from typing import List


def is_end(left, mid, right):
    return mid <= left or right <= mid


def get_init_posi(nums):
    return 0, len(nums) - 1


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        start, end = 1, len(nums)

        nums.sort()
        for m in range(start, end):
            l, r = get_init_posi(nums)

            while not is_end(l, m, r):
                sum3 = nums[l] + nums[m] + nums[r]

                if sum3 == 0:
                    result.add((nums[l], nums[m], nums[r]))
                    l += 1
                if sum3 > 0: r -= 1
                if sum3 < 0: l += 1

        return_ret = [list(ns) for ns in result]
        return return_ret
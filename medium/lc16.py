from typing import List

# 3,97,200
# 1,3,4
# 같은 값이어도 될 듯.

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_diff = 9876543210
        result = 0
        for mi in range(0, len(nums)-1):
            l, r = mi+1, len(nums)-1
            while l < r:
                print(f'{l=},{r=}')
                t = nums[l]+nums[mi]+nums[r]
                diff = abs(target - t)
                if diff < min_diff:
                    min_diff = diff
                    result = t

                if t == target:
                    return t
                if t < target < 0:
                    l+=1
                else:
                    r-=1

        return result

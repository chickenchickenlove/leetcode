from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_diff = 9876543210
        result = 0
        for mi in range(0, len(nums)-1):
            l, r = mi+1, len(nums)-1
            while l < r:
                t = nums[l]+nums[mi]+nums[r]
                diff = abs(target - t)
                if diff < min_diff:
                    min_diff = diff
                    result = t

                if t == target:
                    return t
                if t < target:
                    l+=1
                else:
                    r-=1

        return result


from typing import List
def judge(a, b, l, r):
    return (a != b) and (a != l) and (a != r) and (b != l) and (b != r) and (l != r)

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        targets = [target - n for n in nums]

        length = len(nums)
        result = set()

        print(targets)
        for a, t in enumerate(targets):
            # avoid the duplicates while moving a:
            if a > 0 and nums[a] == nums[a-1]:
                continue
            for b in range(a+1, length):
                l, r = b+1, length-1
                while l < r:
                    ts = nums[l] + nums[r] + nums[b]
                    if ts == t and judge(a, b, l, r):
                        tl = [nums[a], nums[b], nums[l], nums[r]]
                        tl.sort()
                        result.add(tuple(tl))
                    if ts < t:
                        l+=1
                    else:
                        r-=1

        ret = [list(t) for t in result]
        return ret

Solution().fourSum([2,2,2,2,2], 8)
Solution().fourSum([1,0,-1,0,-2,2], 0)

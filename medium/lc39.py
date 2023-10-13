import copy

def sol(nums, idx, carry, target, s, ans):
    if s == target:
        ans.append(copy.copy(carry))

    for i in range(idx, len(nums)):
        if s + nums[i] > target: continue
        carry.append(nums[i])
        sol(nums, i, carry, target, s + nums[i], ans)
        carry.pop()



class Solution:
    from typing import List

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        sol(candidates, 0, [], target, 0, ans)
        return ans




print(Solution().combinationSum([2,3,6,7], 7))









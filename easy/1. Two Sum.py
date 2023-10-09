from typing import List


# 1개의 정해만 있음.
# 똑같은 거 두번 쓸 수 없음.
# 어떤 순서로 값을 반환해도 괜찮음.
# 2개의 숫자를 더해서 target이 되는 값을 찾으면 됨.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        len_nums = len(nums)
        for i in range(len_nums):
            for j in range(len_nums):
                ni, nj = nums[i], nums[j]
                if i == j: continue
                if ni + nj == target: return [i, j]

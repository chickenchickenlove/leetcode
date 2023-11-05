from typing import List
from collections import defaultdict

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        m = defaultdict(int)
        for n in nums:
            m[n] += n

        sorted_list = sorted(list(m.keys()))
        now_buy = [0] * len(sorted_list)
        now_buy[0] = m[sorted_list[0]]

        for idx, num in enumerate(sorted_list):
            if idx == 0: continue
            idx_sum = m[num]

            previous_buy = 0
            if sorted_list[idx]-1 not in m:
                previous_buy = max(previous_buy, now_buy[idx-1] + idx_sum)
            if sorted_list[idx]-1 in m:
                previous_buy = max(previous_buy, now_buy[idx-1], idx_sum)
            if sorted_list[idx]-1 in m and idx-2 >= 0:
                previous_buy = max(previous_buy, now_buy[idx-2] + idx_sum)
            if (idx-3 >= 0) and (sorted_list[idx-3]+1 == sorted_list[idx-2]) and (sorted_list[idx]-1 == sorted_list[idx-1]):
                previous_buy = max(previous_buy, now_buy[idx-3] + idx_sum)

            now_buy[idx] = previous_buy
        return now_buy[-1]

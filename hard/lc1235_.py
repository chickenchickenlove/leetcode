from typing import List
from bisect import bisect_left, bisect_right


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        total_list = [(s, e, p) for s,e,p in zip(startTime, endTime, profit)]
        total_list.sort()

        startTime = [s for s, _, _ in total_list]
        memo = {}

        def rec(idx):

            if idx == len(startTime)-1:
                memo[idx] = total_list[idx][2]

            if idx in memo:
                return memo[idx]

            # 작업을 하는 경우는?
            if idx + 1 < len(startTime):
                memo[idx] = rec(idx+1)


            memo[idx] = max(memo[idx], total_list[idx][2])
            left_idx = bisect_left(startTime, total_list[idx][1])
            right_idx = bisect_right(startTime, total_list[idx][1])

            for i in range(left_idx, right_idx + 1):
                if i < len(startTime):
                    memo[idx] = max(memo[idx], rec(i) + total_list[idx][2], total_list[idx][2])

            return memo[idx]

        return rec(0)

Solution().jobScheduling([1,1,1], [2,3,4], [5,6,4])

# Solution().jobScheduling([1,2,3,3],[3,4,5,6],[50,10,40,70])
# Solution().jobScheduling([4,2,4,8,2],[5,5,5,10,8],[1,2,8,10,4])
# Solution().jobScheduling([6,15,7,11,1,3,16,2], [19,18,19,16,10,8,19,8], [2,9,1,19,5,7,3,19])
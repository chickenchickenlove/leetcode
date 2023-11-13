from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        N = len(events)
        events.sort()

        memo = {}
        starts = [s for s, _, _ in events]

        # 구매 가능한 횟수, 현재 인덱스
        def rec(buy_count, idx):
            nonlocal k
            if idx >= len(events) or buy_count == 0:
                return 0

            if (buy_count, idx) in memo:
                return memo[(buy_count, idx)]

            # 안사고, 다음 번에 사는 것을 탐색
            memo[(buy_count, idx)] = rec(buy_count, idx+1)

            # 사고, 다음번을 탐색
            end = events[idx][1] + 1
            a = bisect_left(starts, end)
            b = bisect_right(starts, end)
            t = events[idx][2]

            # 사고 + 다음에도 삼.
            for i in range(a, b+1):
                if i > len(events)-1:
                    break
                if buy_count+1 < k:
                    continue

                t = max(t, rec(buy_count-1, i) + events[idx][2])
            memo[(buy_count, idx)] = max(t, memo[(buy_count, idx)])
            return memo[(buy_count, idx)]

        return rec(k, 0)

#

Solution().maxValue([[1,2,4],[3,4,3],[2,3,1]], 2)
Solution().maxValue([[1,2,4],[3,4,3],[2,3,10]], 2)
Solution().maxValue([[1,1,1],[2,2,2],[3,3,3],[4,4,4]], 3)
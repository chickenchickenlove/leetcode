from typing import List

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        new_cuts = sorted((cuts + [0, n]))
        memo = {}

        def cost(start, end):

            if (start, end) in memo:
                return memo[(start, end)]
            # 나눌 수 없는 경우.
            if end - start <= 1:
                memo[(start, end)] = 0
                return 0

            ret = min(cost(start, i) + cost(i, end) for i in range(start+1, end)) + new_cuts[end] - new_cuts[start]
            memo[(start, end)] = ret
            return ret

        return cost(0, len(new_cuts)-1)
















# Solution().minCost(7, [1,2])
Solution().minCost(7, [1,3,4,5])
Solution().minCost(9, [5,6,1,4,2])
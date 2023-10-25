from typing import List
from collections import defaultdict


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        left_array = [0 for _ in range(n)]
        right_array = [0 for _ in range(n)]

        mi = 999999999
        ma = 0
        for i, k in enumerate(prices):
            mi = min(k, mi)
            ma = max(ma, k-mi)
            left_array[i] = ma
        # print(left_array)

        ma = 0
        mv = 0
        for i in range(len(prices)-1, -1, -1):
            ma = max(ma, prices[i])
            mv = max(mv, ma - prices[i])
            right_array[i] = mv

        result = max(left_array[0], left_array[-1], right_array[0], right_array[-1])
        for i in range(n-1):
            result = max(result, left_array[i] + right_array[i+1])

        print(left_array)
        print(right_array)
        print(result)
        return result



# Solution().maxProfit([0,1,2,3,4])
# Solution().maxProfit([6,1,3,2,4,7])
# Solution().maxProfit([1,2,3,4,5])
# Solution().maxProfit([1,2,6,0,6])
# Solution().maxProfit([3,3,5,0,0,3,1,4])
# Solution().maxProfit([7,1,5,3,6,4])
Solution().maxProfit([1,2,3,4,5])
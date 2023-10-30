from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        if n == 1 :
            return triangle[0][0]

        for i in range(1, n):
            for j in range(len(triangle[i])):
                now_value = triangle[i][j]
                if j == 0:
                    triangle[i][j] = triangle[i-1][0] + now_value
                elif j == len(triangle[i]) - 1:
                    triangle[i][j] = triangle[i-1][-1] + now_value
                else:
                    triangle[i][j] = min(triangle[i-1][j-1], triangle[i-1][j]) + now_value

        return min(triangle[-1])

















Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])

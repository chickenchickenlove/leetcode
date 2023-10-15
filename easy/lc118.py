
from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(1, numRows):
            r = [1]
            for j in range(len(ans[i-1])-1):
                r.append(ans[i-1][j] + ans[i-1][j+1])
            r.append(1)
            ans.append(r)

        return ans

s = Solution()
s.generate(5)
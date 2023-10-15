
from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        for i in range(1, rowIndex+1):
            r = [1]
            for j in range(len(ans)-1):
                r.append(ans[j] + ans[j+1])
            r.append(1)
            ans = r
        return ans

s = Solution()
print(s.generate(3))
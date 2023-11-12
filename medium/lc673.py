from typing import List

# length[i]는 i번째를 반드시 포함한 증가하는 수열의 길이임.
# 이 수열의 최대 길이를 달성할 수 있는 가지수를 추가하는 방식으로도 처리할 수 있음.
# 이전 LIS에는 뒤에서부터 올라왔음. (포함하고, 안 포함하고의 개념으로...)

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        length = [1] * N
        count = [1] * N

        for i in range(1, N):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = 0
                    if length[j] + 1 == length[i]:
                        count[i] += count[j]

        REAL_MAX = max(length)
        ans = 0

        for i, v in enumerate(length):
            if v == REAL_MAX:
                ans += count[i]
        return ans

Solution().findNumberOfLIS([1,2,4,3,5,4,7,2])
Solution().findNumberOfLIS([1,3,5,4,7])
Solution().findNumberOfLIS([2,2,2,2,2])




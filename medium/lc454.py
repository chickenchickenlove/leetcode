from typing import List
from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        nums3.sort()
        nums4.sort()

        n1 = defaultdict(int)
        for i1, v1 in enumerate(nums1):
            for i2, v2 in enumerate(nums2):
                n1[v1+v2] += 1

        n2 = defaultdict(int)
        for i3, v3 in enumerate(nums3):
            for i4, v4 in enumerate(nums4):
                n2[v3+v4] += 1

        result = 0
        for k, v in n1.items():
            result += n2[-k] * v

        return result

# print(Solution().fourSumCount([1,2], [-2,-1], [-1,2], [0,2]))
print(Solution().fourSumCount([-1,-1], [-1,1], [-1,1], [1,-1]))







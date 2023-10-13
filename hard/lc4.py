from typing import List

#first
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for n in nums2:
            nums1.append(n)

        len_nums1 = len(nums1)
        nums1.sort()
        mid = (len_nums1 // 2) - 1

        if len_nums1 % 2 == 1:
            return nums1[mid + 1]
        else:
            return (nums1[mid] + nums1[mid+1]) / 2
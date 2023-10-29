from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [nums[0]]

        for num in nums[1:]:
            if num > sub[-1]:
                sub.append(num)
            else:
                # Find the first element in sub that is greater than or equal to num
                i = 0
                while num > sub[i]:
                    i += 1
                sub[i] = num

        return len(sub)
Solution().lengthOfLIS([10,9,2,5,3,7,101,18])

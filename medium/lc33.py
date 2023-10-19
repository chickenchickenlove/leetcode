def get_func(number, length):
    if number >= length:
        return number - length
    return number

from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = nums
        l, r = 0, len(nums)-1
        max_value = max(n[l], n[r])
        max_value_idx = l if n[l] > n[r] else r

        # 최대값 찾기
        while l <= r:
            m = (l+r)//2
            if n[l] > max(n[m], n[r]):
                if n[l] > max_value:
                    max_value = n[l]
                    max_value_idx = l
                r = m-1
            else:
                if n[m] > n[r] and n[m] > max_value:
                    max_value = n[m]
                    max_value_idx = m
                elif n[m] < n[r] and n[r] > max_value:
                    max_value = n[r]
                    max_value_idx = r
                l = m+1

        # 최대값부터 2배해서 찾기
        l = max_value_idx + 1
        r = max_value_idx + len(nums)

        while l <= r:
            m = (l+r)//2
            ml = get_func(m, len(nums))
            if n[ml] == target:
                return ml
            elif n[ml] < target:
                l = m+1
            else:
                r = m-1
        return -1


print(Solution().search([4,5,6,7,0,1,2],0))
# print(Solution().search([1],0))
# print(Solution().search([1,3],1))
# print(Solution().search([3,1],0))

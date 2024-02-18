class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        carry = nums[0]
        if n == 1:
            return True

        for i in range(1, n):
            if carry <= 0:
                return False
            carry = max(carry-1, nums[i])
        return True
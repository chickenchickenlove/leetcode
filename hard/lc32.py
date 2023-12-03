

# 없어질 때 마다 1개씩 늘리면 될 듯?
# 연속해서 없어지면 1개씩 늘리면 되고
# 안 연속해서 없어지면 끝.
class Solution:
    def longestValidParentheses(self, s: str) -> int:

        n = len(s)
        if n <= 1: return 0

        dp = [0 for _ in range(n)]

        for i in range(1, n):

           if s[i-1] == '(' and s[i] == ')':
               dp[i] += 2
               if i-2 >= 0:
                   dp[i] += dp[i-2]
           elif s[i-1] == ')' and s[i] ==')':
               nidx = dp[i-1] + 1
               if i-nidx >= 0 and s[i-nidx] == '(':
                   dp[i] += dp[i-1] + 2 + dp[i-nidx-1]

            # 0 2 0 0 2 4
            # ()(())
        # print(dp)
        return max(dp)

Solution().longestValidParentheses('()(())')
Solution().longestValidParentheses(')()())')

# '020406'
# '()()()'
#
# i-dp[i-1]-1 == '(' -> dp[i] = 2 + dp[i-1] + dp[i-dp[i-1]]
# '0002'
# '((()))'
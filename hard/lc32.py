

# 없어질 때 마다 1개씩 늘리면 될 듯?
# 연속해서 없어지면 1개씩 늘리면 되고
# 안 연속해서 없어지면 끝.
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return 0
        m = 0
        stack = []

        for i, a in enumerate(s):
            if a == '(':
                stack.append(i)
            else:
                # stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    m = max(m, i - stack[-1])
                    # stack.append(i)

        print(m)
        return m



for s in ["()(()", " ()(())"]:
    Solution().longestValidParentheses(s)

# 더 많아지는 순간 끊겼다고 볼 수 있을 듯?
# ()(((()))))
# )())))


# 12
# 2칸으로 끝나지는 않음.
#
# ((()))((()))
# (((((((((())
# ((())))((()) -> 6이어야 함.
# ) > ( 이거일 때 문제가 됨. 즉, 이렇게 될 때, 연속이 끊김.
# (()(()((((( -> 이런 경우도 있을 듯? 2개인데.
# 없어졌을 때를 기준으로 )가 나타나면, 괜찮을 듯 ???
# ((((((()(((()))
# (((()()())))
# Pop () 할 때 마다 count + 1을 하면 됨.
from dataclasses import dataclass
@dataclass(frozen=True)
class Record:
    s: str
    p: str

    def get(self):
        return self.s, self.p


        # a* -> 무조건 한 덩어리로 취급해야 함.  두 칸을 넘겼다고 해보자.
        # a*a
        # a인 경우라면 어떻게 해야할까?
        # 1. a*를 무시하고 넘긴다.
        # 2. a를 매칭하고 넘긴다.
        # 즉, 이 과정을 둘다 탐색해야한다. 어떤 경우는 맞을 수도 있고, 어떤 경우는 틀릴 수도 있기 때문이다.
        # 재귀적으로 해서, 마지막에 True라는 값을 넘겨야 할 것 같음.

# 이건 이제 timeout이 발생함.

class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        def sol(record, si, pi):
            s, p = record.get()
            if len(s) == si and len(p) == pi:
                return True
            if len(p) == pi:
                return False

            result = [0]
            # *가 있는 경우
            if pi+1 < len(p) and p[pi+1] == '*':
                # 현재 문자에 매칭되지 않는 것으로 판단하고 다음으로 넘김.
                if sol(record, si, pi + 2):
                    return True
                # 현재 문자에 매칭되는 것으로 판단하고, 문자열 매칭 판정하고 넘김.
                if len(s) > si and (p[pi] == s[si] or p[pi] == '.'):
                    if sol(record, si+1, pi):
                        return True
            else:
                if len(p) > pi and len(s) > si and (p[pi] == s[si] or p[pi] == '.'):
                    if sol(record, si+1, pi+1):
                        return True
                    # result.append(sol(record, si+1, pi+1))

            return max(result)

        record = Record(s, p)
        a = sol(record, 0, 0)
        return a == 1








s = Solution()
# print(s.isMatch('aa', 'a') == False)
# print(s.isMatch('aa', 'a*') == True)
# print(s.isMatch('ab', '.*') == True)
# print(s.isMatch('aab', 'c*a*b') == True)
# print(s.isMatch("mississippi", "mis*is*p*.") == True)

# print(s.isMatch("mppi", "mp*.") == True)
# print(s.isMatch("aaaaaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*") == False)
print(s.isMatch("aaaaaaaaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*") == False)
# print(s.isMatch("aa", ".*.") == True)
# print(s.isMatch("aaa", "a*a") == True)
# print(s.isMatch("abcd", "d*") == False)
# print(s.isMatch("aaa", "ab*a*c*a") == True)
# print(s.isMatch("ab", ".*c") == False)
# print(s.isMatch("aaa", "aaaa") == False)
#
#
# # """ aaaaaaaa a*aaaa """
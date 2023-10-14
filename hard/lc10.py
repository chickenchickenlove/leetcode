def add(stack, s, count):
    stack.append(s)
    return count + 1

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pidx = 0
        iter_cnt = 0

        # Match된 녀석들은 stack에 넣는다.
        # 만약에 안되었으면 어디까지 뽑아야 하지?
        stack = []

        # 반복 플래그가 켜진거, 마지막 문자 무엇인지 기억
        can_repeat = False
        last = ''

        for string in s:
            if pidx == len(p): return False
            iter_cnt += 1
            if string == p[pidx]:
                stack.append(p[pidx])
                pidx += 1
                last = string
                can_repeat = False
            elif p[pidx] == '.':
                stack.append(p[pidx])
                pidx +=1
                last = '.'
                can_repeat = False
            elif p[pidx] == '*':
                if stack[-1] == string or stack[-1] == '.':
                    stack.append('*')
                    pidx += 1
                    can_repeat = True
                # 매칭 안되는 경우.
                else: return False
            else:
                if (last == '.' or last == string) and can_repeat: continue
                else:
                    ppidx = pidx

                    for pp in range(ppidx, len(p)):

                        # 그 다음칸을 볼 수 있는 경우
                        if pp + 1 < len(p):
                            if p[pp+1] == '*':
                                stack.append(p[pidx])
                                pidx += 1
                                stack.append(p[pidx])
                                pidx += 1

                        if pidx == len(p): return False
                        if p[pidx] == string:
                            stack.append(p[pidx])
                            pidx +=1
                            break
                        else: return False







        # print(iter_cnt == len(s) and pidx == len(p))
        return iter_cnt == len(s) and pidx == len(p)

            # 현재값이 매칭되는 경우. ->
            # 그 값을 stack에 넣고 pidx + 1

            # 현재값이 매칭되지 않는 경우.
            # (.)인 경우 -> 모든 문자에 매칭된다는 것임. -> 하고 넘기면 될 듯.
            # (*)인 경우 -> 앞에 있는 값의 여부에 따라 나누어짐












s = Solution()
# print(s.isMatch('aa', 'a') == False)
# print(s.isMatch('aa', 'a*') == True)
# print(s.isMatch('ab', '.*') == True)
# print(s.isMatch('aab', 'c*a*b') == True)
# print(s.isMatch("mississippi", "mis*is*p*.") == False)
# print(s.isMatch("aaa", "a*a") == True)
print(s.isMatch("abcd", "d*") == True)
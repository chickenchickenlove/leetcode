


'''
()()()
()()
()

n = 1 ()
n = 2 ()() (())
n = 3 ()()() (()()) (())() ()(()) ((()))

# 1을 구한다
# 2: 1에다가 ( ) 하는 작업, ()를 추가하는 작업을 한다. 그러니까 1개를 추가하는 작업
# 3: 2에다가 ()() 여기에 (), ( ) 하는 방법.     (()) -> (), ( ) 하는 방법 한다.
# 4: 이게 필요함. (())(())
'''

import copy

# 좌우가 다름. 중복 제거 한번 해야할 듯.
# (())(()) 이게 없음.

def get_wrap(v):
    hs = set()
    for s in v:
        for i in range(len(s)):
            hs.add(''.join(['(', s[:i], ')', s[i:]]))
    return list(hs)

from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        v = ['()']
        if n == 1:
            return v
        for i in range(1, n):
            v = get_wrap(v)
        return v

print(len(Solution().generateParenthesis(4)))



















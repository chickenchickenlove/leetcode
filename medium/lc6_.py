class Solution:
    def convert(self, s: str, numRows: int) -> str:
        d = True
        r, c = 0, 0
        rs = [[] for _ in range(numRows)]
        if numRows == 1 : return s

        for a in s:
            rs[r].append(a)

            if r == (numRows - 1):
                d = False
            elif r == 0:
                d = True
            if d:
                r += 1
            else:
                r -= 1
                c += 1
        return ''.join([''.join(a) for a in rs])

Solution().convert('ABC', 1)
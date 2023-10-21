from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        lr, lc = len(grid), len(grid[0])
        g = grid
        # d = [[2000 for _ in range(lc)] for _ in range(lr)]
        # d[0][0] = g[0][0]

        for r in range(lr):
            for c in range(lc):
                if r == 0 and c == 0: continue
                match -1 < r-1, -1 < c-1:
                    case False, _ :
                        g[r][c] = g[r][c-1]+g[r][c]
                    case _, False:
                        g[r][c] = g[r-1][c]+g[r][c]
                    case True, True:
                        g[r][c] = min(g[r-1][c] + g[r][c], g[r][c-1] + g[r][c])
        return g[lr-1][lc-1]



    # def minPathSum(self, grid: List[List[int]]) -> int:
    #     lr, lc = len(grid), len(grid[0])
    #     g = grid
    #     d = [[1000 for _ in range(lc)] for _ in range(lr)]
    #     v = [[0 for _ in range(lc)] for _ in range(lr)]
    #     d[0][0] = g[0][0]
    #
    #     q = deque([(0, 0)])
    #     while q:
    #         r, c = q.popleft()
    #         if v[r][c] != 0 : continue
    #         v[r][c] = 1
    #
    #         for x, y in MOVE:
    #             nr, nc = r+x, c+y
    #             if -1 < nr < lr and -1 < nc < lc:
    #                 q.append((nr, nc))
    #                 d[nr][nc] = min(d[nr][nc], d[r][c] + g[nr][nc])
    #         print(len(q))
    #
    #     return d[lr-1][lc-1]
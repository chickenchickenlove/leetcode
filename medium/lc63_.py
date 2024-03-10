from typing import List
from collections import deque
MOVE = [[0,1], [1,0]]


class Solution:
    # DP
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        lr, lc = len(obstacleGrid), len(obstacleGrid[0])
        d = [[0 for _ in range(lc)] for _ in range(lr)]
        g = obstacleGrid

        if g[lr-1][lc-1] == 1 or g[0][0] == 1:
            return 0

        d[0][0] = 1

        for r in range(lr):
            for c in range(lc):
                if g[r][c] == 1 or (r == 0 and c == 0): continue
                match -1 < r-1, -1 < c-1:
                    case False, _:
                        d[r][c] += d[r][c-1]
                    case _, False:
                        d[r][c] += d[r-1][c]
                    case _, _:
                        d[r][c] += d[r-1][c] + d[r][c-1]
        return d[lr-1][lc-1]


    # BFS + DP
    def uniquePathsWithObstacles_BFS_DP(self, obstacleGrid: List[List[int]]) -> int:
        lr, lc = len(obstacleGrid), len(obstacleGrid[0])
        d = [[0 for _ in range(lc)] for _ in range(lr)]
        v = [[0 for _ in range(lc)] for _ in range(lr)]
        g = obstacleGrid

        # Corner case
        if g[0][0] == 1:
            return 0

        d[0][0] = 1
        q = deque([(0, 0)])

        while q:
            r, c = q.popleft()
            if v[r][c] != 0: continue
            v[r][c] = 1

            for move in MOVE:
                next_r, next_c = r + move[0], c + move[1]

                if -1 < next_r < lr and -1 < next_c < lc and g[next_r][next_c] != 1:
                    d[next_r][next_c] += d[r][c]
                    q.append((next_r, next_c))

        return d[lr-1][lc-1]
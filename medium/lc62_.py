from collections import deque
MOVE = [[0,1], [1,0]]
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d = [[0 for _ in range(n)] for _ in range(m)]
        v = [[0 for _ in range(n)] for _ in range(m)]
        d[0][0] = 1

        q = deque([(0, 0)])

        while q:
            r, c = q.popleft()

            # 이 조건을 통해서 해결할 수 있음.
            # 여러군데서의 합은 처리할 수 있으며, 여기서 나가는 것은 한번만으로 정해버림.
            if v[r][c] != 0:
                continue
            v[r][c] = 1

            # 보낼 때 값을 더하는게 나을 듯.
            for move in MOVE:
                next_r, next_c = r+move[0], c+move[1]

                if -1 < next_r < m and -1 < next_c < n:
                    d[next_r][next_c] += d[r][c]
                    q.append((next_r, next_c))
        return d[m-1][n-1]

def bfs(jump_map, start, end):
    visit_list = [0 for _ in range(len(jump_map))]
    end_list = [0 for _ in range(len(jump_map))]
    for e in end:
        end_list[e] = 1

    q = deque([start])

    while q:
        now_position = q.popleft()
        jump_range = jump_map[now_position]

        if end_list[now_position] == 1:
            return True

        next_position_nega = now_position - jump_range
        if next_position_nega >= 0 and visit_list[next_position_nega] == 0:
            visit_list[next_position_nega] = 1
            q.append(next_position_nega)

        next_position_posi = now_position + jump_range
        if next_position_posi < len(visit_list) and visit_list[next_position_posi] == 0:
            visit_list[next_position_posi] = 1
            q.append(next_position_posi)


    return False

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        end = []
        for i, n in enumerate(arr):
            if n == 0:
                end.append(i)
        return bfs(arr, start, end)
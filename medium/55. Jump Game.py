'''
- 0번 인덱스에서 시작. 마지막 인덱스에 도착할 수 있으면 True, 아니면 False
- 각 배열은 몇번 띌 수 있는지를 의미. 즉, now + <0 ~ 값>까지 가능함.
- 왼 / 오른쪽 다 갈 수 있을 수도 있음.

- 방문한 적이 있다면, 이미 센 경우의 수니 셀 필요가 없음.
- 왼 / 오른쪽으로 덱에 집어넣는다. 이 때, 점프 가능한 횟수를 넣자.
   - 방문한 적이 없는 녀석이면 덱에 넣는다.

length = 10_000
nums[i] = 100_000


'''
from typing import List
from collections import deque

def bfs(jump_map):
    visit_list = [0 for _ in range(len(jump_map))]
    end = len(jump_map) - 1
    q = deque([0])

    while q:
        now_position = q.popleft()
        jump_range = jump_map[now_position]

        for diff in range(-jump_range, jump_range + 1):
            next_position = now_position + diff
            if next_position == end:
                return True
            if next_position < 0 or next_position > end:
                continue
            if visit_list[next_position] == 0:
                visit_list[next_position] = 1
                q.append(next_position)
    return False


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return bfs(nums)



### Other Solution
'''
- 내가 걸을 수 있는 걸음수 = k 
- 한칸씩 걷는다고 가정하고, 더 큰 걸음이 가능한 경우 이것을 선택한다.
- 그러나 이것은 오른쪽으로만 걷는 전제하에서 동작한다. 
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        k = nums[0]
        for i in range(len(nums)-1):
            if nums[i] > k:
                k = nums[i]
            k = k - 1
            if k < 0 :
                return False
        return True
'''

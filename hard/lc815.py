from typing import List
from collections import defaultdict

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        bus_station = defaultdict(set)
        for idx, route in enumerate(routes):
            for station in route:
                bus_station[station].add(idx)

        def bfs(start, target):
            from collections import deque

            bus_visit = [0] * len(routes)
            station_visit = defaultdict(int)

            q = deque([(start, 0)])

            while q:
                now, cnt = q.popleft()

                if now == target:
                    return cnt

                for bus in bus_station[now]:
                    if bus_visit[bus] == 1:
                        continue
                    bus_visit[bus] = 1

                    for bus_routes in routes[bus]:
                        if station_visit[bus_routes] == 0:
                            station_visit[bus_routes] = 1
                            q.append((bus_routes, cnt+1))
            return -1

        return bfs(source, target)
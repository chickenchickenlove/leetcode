from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        start = 0
        for i in range(n):
            if height[i] != 0:
                start = i
                break
        max_value = previous = height[start]
        stack = [max_value]

        ans = 0
        for i in range(start+1, n):
            now = height[i]

            # 내림차순이라면, 그냥 추가하면 됨.
            if now == max_value and not(now > previous):
                continue
            elif now > previous:
                # 2 0 1인 경우, stack and stack[-1] < now -> Now보다 작은게 있을 떄 까지
                if (stack and stack[-1] < now) and max_value > now:
                    i = len(stack)-1
                    while stack[i] < now:
                        skew = now - stack[i]
                        stack[i] = now
                        ans += skew
                        i-=1

                # 2 0 3인 경우, stack and stack[-1] != Max인 경우. -> 이 때는 Max일 때까지
                elif (stack and stack[-1] < now) and max_value <= now:
                    i = len(stack)-1
                    while stack[i] != max_value:
                        skew = max_value - stack[i]
                        stack[i] = max_value
                        ans += skew
                        i-=1
                    max_value = now

            stack.append(now)
            previous = now
        return ans


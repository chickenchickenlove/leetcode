import sys

N, X = list(map(int, sys.stdin.readline().split()))
S = list(map(int, sys.stdin.readline().split()))

ans = 0
for s in S:
    if s <= X:
        ans+=s

print(ans)

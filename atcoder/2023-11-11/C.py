import sys

N, Q = list(map(int, sys.stdin.readline().split()))
S = str(sys.stdin.readline().rstrip())

dpl = [0]*(N+1)

for i in range(N):
    si = i-1
    dpl[i] = dpl[i-1]
    if S[si] == S[si+1]:
        dpl[i] += 1

dpl[-1] = dpl[-2]


for _ in range(Q):
    l, r = list(map(int, sys.stdin.readline().split()))
    ans = dpl[r-1] - dpl[l-1]
    print(ans)

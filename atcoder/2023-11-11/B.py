import sys

N = int(sys.stdin.readline().rstrip())
D = list(map(int, sys.stdin.readline().split()))

ans = 0

dp = [0] * N
# 똑같은 숫자 하나씩 붙이면 될 듯?

for i in range(1, N+1):
    for d in range(1, D[i-1]+1):
        temp = str(i) + str(d)

        my_set = {s for s in str(temp)}
        if len(my_set) == 1 :
            dp[i-1] += 1

print(sum(dp))







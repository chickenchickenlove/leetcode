import sys
S = str(sys.stdin.readline().rstrip())
stack = []
for s in S:
    stack.append(s)
    if len(stack) > 2:
        if stack[-3] == 'A' and stack[-2] == 'B' and stack[-1] == 'C':
            for _ in range(3):
                stack.pop()
print(''.join(stack))
















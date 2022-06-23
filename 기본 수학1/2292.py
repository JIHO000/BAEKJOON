N = int(input())
honeycomb = 1
cnt = 1
while honeycomb < N:
    honeycomb += 6 * cnt
    cnt += 1
print(cnt)
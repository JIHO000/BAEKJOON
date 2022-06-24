import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    count = 0
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        d1 = (((x1 - cx) ** 2) + ((y1 - cy) ** 2)) ** 0.5
        d2 = (((x2 - cx) ** 2) + ((y2 - cy) ** 2)) ** 0.5
        if r > d1 and r > d2:
            pass
        elif r > d1:
            count += 1
        elif r > d2:
            count += 1
    print(count)

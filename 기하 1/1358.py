import sys

input = sys.stdin.readline

W, H, X, Y, P = map(int, input().split())
count = 0
for _ in range(P):
    px, py = map(int, input().split())
    r = (H/2)
    pr1 = ((X - px) ** 2 + (Y + (H/2) - py) ** 2) ** 0.5
    pr2 = ((X + W - px) ** 2 + (Y + (H/2) - py) ** 2) ** 0.5
    if (X <= px <= X+W) and (Y <= py <= Y+H):
        count += 1 
    elif pr1 <= r or pr2 <= r:
        count += 1
print(count)

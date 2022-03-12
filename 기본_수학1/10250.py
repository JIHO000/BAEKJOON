n = int(input())
for _ in range(n):
    H, W, guest = map(int, input().split())
    if guest % H == 0:
        print(f"{H}{guest//H:02d}")
    else:
        print(f"{guest%H}{guest//H+1:02d}")
N = int(input())
cnt = 2
while N != 1:
    if N % cnt == 0:
        print(cnt)
        N //= cnt
    else:
        cnt += 1
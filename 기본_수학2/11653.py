N = int(input())
cnt = 2
while N != 1:
    for i in range(cnt, int(N**.5) + 1):
        if N % i == 0:
            print(i)
            N //= i
            cnt = i
            break
    else:
        print(N)
        break
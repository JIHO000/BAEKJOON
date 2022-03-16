N = int(input())
min = N - 9*len(str(N))
min = 1 if min<1 else min

for i in range(min, N+1):
    num = sum(map(int,str(i)))
    sum_num = i + num
    if N == sum_num:
        print(i)
        break
else:
    print(0)
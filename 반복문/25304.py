X = int(input())
N = int(input())
sum_X = 0 
count = 0
for _ in range(N):
    a, b = map(int, input().split())
    sum_X += a*b
    count += 1

if X == sum_X and N == count:
    print("Yes")
else:
    print("No")
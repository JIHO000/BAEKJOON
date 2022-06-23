N = int(input())
group = []
for _ in range(N):
    *a, =map(int,input().split())
    group.append(a)

for i in group:
    rank = 1
    for j in group:
        rank += 1 if i[0] < j[0] and i[1] < j[1] else 0
    print(rank, end=" ")
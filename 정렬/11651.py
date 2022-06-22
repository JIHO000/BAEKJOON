n = int(input())

list_xy = []
for _ in range(n):
    list_xy.append(list(map(int, input().split())))

list_xy.sort(key=lambda x: (x[1], x[0]))

for i in list_xy:
    print(i[0], i[1])

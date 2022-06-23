n = int(input())
list = []
for i in range(n):
    A, B = map(int, input().split())
    list.append([A, B])
for i in range(n):
    print(list[i][0]+list[i][1])


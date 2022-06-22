import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dic = {}
for i in range(1, n + 1):
    name = input().rstrip()
    dic[i] = name
    dic[name] = i

for _ in range(m):
    search_name = input().rstrip()
    if search_name.isdigit():
        print(dic[int(search_name)])
    else:
        print(dic[search_name])
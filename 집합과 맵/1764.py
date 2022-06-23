import sys

input = sys.stdin.readline
n, m = map(int, input().split())

dic = {}
for i in range(n + m):
    name = input().rstrip()
    if name not in dic:
        dic[name] = 1
    else:
        dic[name] += 1

result = [i for i, v in dic.items() if v >= 2]
result.sort()
print(len(result))
for i in result:
    print(i)
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

S = set()

for _ in range(n):
    S.add(input())
array = []
for _ in range(m):
    array.append(input())
print(sum([i in S for i in array]))
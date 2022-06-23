import sys

N, X = map(int, input().split())
data = list(map(int, sys.stdin.readline().split()))
for i in [num for num in data if num < X]:
    print(i)

import sys

n = int(input())
card = list(map(int, sys.stdin.readline().split()))
m = int(input())
check = list(map(int, sys.stdin.readline().split()))

hash = {}

for i in card:
    if i in hash:
        hash[i] += 1
    else:
        hash[i] = 1

for i in check:
    if i in hash:
        print(hash[i], end=' ')
    else:
        print(0, end=' ')
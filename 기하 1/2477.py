from collections import defaultdict
import sys
input = sys.stdin.readline

fruit = int(input())
area = defaultdict(list)

for i in range(6):
    dir, length = map(int, input().split())
    area[dir].append(length,i)

max_length_idx = []
min_length_idx = []
for i in area:
    if len(area[i]) == 1:
        max_length_idx.append(i)
        idx = 1
    else:
        min_length_idx.append(i)
        idx = 0

if idx == 0:
    ans = area[max_length_idx[0]][0] * area[max_length_idx[1]][0] - area[min_length_idx[0]][1] * area[min_length_idx[1]][0]
else:
    ans = area[max_length_idx[0]][0] * area[max_length_idx[1]][0] - area[min_length_idx[0]][0] * area[min_length_idx[1]][1]

print (ans * fruit)

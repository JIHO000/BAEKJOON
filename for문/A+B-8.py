import sys
n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))
    print(f"Case #{i +1}:{date[i][0]} + {data[i][1]} = {data[i][0]+data[i][1]} ")
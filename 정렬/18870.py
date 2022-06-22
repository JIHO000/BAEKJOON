import sys

n = int(sys.stdin.readline())
X1 = list(map(int, sys.stdin.readline().split()))
X2 = list(set(X1))
X2.sort()
dic = {X2[i] : i for i in range(len(X2))}
for i in X1:
    print(dic[i], end=" ")
import sys
rec =[]
for _ in range(3):
    x, y = map(int,sys.stdin.readline().split())
    rec.append([x,y])
print(rec[0][0]^rec[1][0]^rec[2][0], rec[0][1]^rec[1][1]^rec[2][1])
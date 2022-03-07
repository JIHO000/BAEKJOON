a = int(input())
b = list(map(int,input()))
c = 0
for i, j in enumerate(reversed(b)):
    print(a*j)
    c += j * 10**i
print(a*c)

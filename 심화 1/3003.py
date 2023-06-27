ori = [1, 1, 2, 2, 2, 8]
sub = list(map(int,input().split()))

for i in range(6):
    print(ori[i]-sub[i], end= " ")
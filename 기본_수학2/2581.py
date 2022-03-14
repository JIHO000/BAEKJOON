N, M = map(int,input().split())
demical_list=[]

for i in range(N,M + 1):
    if i != 1:
        for j in range(2, int(i**.5)+1):
            if i % j == 0:
                break
        else:
            print(i)
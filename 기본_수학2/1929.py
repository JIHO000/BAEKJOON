N, M = map(int,input().split())
demical_list=[True] *(M+1)
for i in range(2, int(M**.5) + 1):
    if demical_list[i] == True:
        for j in range(i+i, M+1, i):
            demical_list[j] = False
for i in range(N,M+1):
    if demical_list[i] == True:
        print(i)
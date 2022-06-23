M, N = map(int,input().split())
demical_list=[True] *(N+1)
for i in range(2, int(N**.5) + 1):
    if demical_list[i] == True:
        for j in range(i+i, N+1, i):
            demical_list[j] = False
for i in range(M,N+1):
    if demical_list[i] == True:
        if i != 1:
            print(i)
T = int(input())
for _ in range(T):
    n = int(input())
    demical_list=[True] *(n+1)
    for i in range(2, int(n**.5) + 1):
        if demical_list[i] == True:
            for j in range(i+i, n+1, i):
                demical_list[j] = False

    for i in range(n//2,1,-1):
        if demical_list[i] and demical_list[n - i]:
            print(i, n-i)
            break
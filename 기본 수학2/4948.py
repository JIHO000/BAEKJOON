while True:
    M = int(input())
    if M == 0:
        break
    N = M *2
    cnt =0
    demical_list=[True] *(N+1)
    for i in range(2, int(N**.5) + 1):
        if demical_list[i] == True:
            for j in range(i+i, N+1, i):
                demical_list[j] = False
    for i in range(M+1,N+1):
        if demical_list[i] == True:
            if i != 1:
                cnt += 1
    print(cnt)
    
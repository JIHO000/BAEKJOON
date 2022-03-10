N = int(input())
if N < 100:
    print(N)
else:
    result = 99
    for i in range(100, N + 1):
        X = list(map(int, str(i)))
        j = 0
        while X[j] - X[j+1] == X[j+1] - X[j+2]:
            j += 1
            if j == len(X) - 2:
                result += 1
                break
    print(result)
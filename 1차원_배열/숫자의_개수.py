import collections
A = []
result = 1
for i in range(3):
    A.append(int(input()))
    result *= A[i]
A = collections.Counter(map(int,list(str(result))))
for i in range(10):
    print(A[i])
    
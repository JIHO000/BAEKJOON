N,M = map(int, input().split())

basket = [i for i in range(1,N+1)]
tmp = []

for i in range(M):
    i,j = map(int, input().split())
    tmp = basket[i-1:j]
    tmp.reverse()
    basket[i-1:j] =tmp

for i in range(N):
    print(basket[i], end = ' ')
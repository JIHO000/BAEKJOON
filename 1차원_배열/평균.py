N = int(input())
data = list(map(int, input().split()))
print(sum([num for num in data])/max(data)*100/N)
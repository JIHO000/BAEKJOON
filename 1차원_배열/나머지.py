import collections
data = collections.defaultdict(int)
for i in range(10):
    data[int(input()) % 42] += 1
print(len(data))

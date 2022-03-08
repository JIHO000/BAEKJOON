data = []
for i in range(9):
    a = int(input())
    data.append(a)
b=max(data)
print(b)
print(data.index(b)+1)
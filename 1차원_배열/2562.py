data = []
for i in range(9):
    data.append(int(input()))
b=max(data)
print(b)
print(data.index(b)+1)
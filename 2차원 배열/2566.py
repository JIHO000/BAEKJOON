grid = []
max_row = -1
max_colomn = -1
max_row_value = -1
max_value = -1
for i in range(9):
    grid.append(list(map(int,input().split())))
    max_row_value = max(grid[i])
    if max_row_value > max_value:
        max_value = max_row_value
        max_row = i
        max_colomn = grid[i].index(max_value)

print(max_value)
print(max_row + 1, max_colomn + 1)
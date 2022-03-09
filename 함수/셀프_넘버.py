natural_num = set(range(1, 10001))
remove_num = set()
for i in range(1, 10001):
    *num, = map(int, str(i))
    n = i + sum(num)
    remove_num.add(n)
self_num = sorted(natural_num - remove_num)
for i in self_num:
    print(i)
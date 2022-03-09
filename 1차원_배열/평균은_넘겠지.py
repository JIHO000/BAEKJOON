import sys
for _ in range(int(input())):
    n, *data = map(int, sys.stdin.readline().split())
    print("%.3f%%" % (len([num for num in data if num > sum(data)/n])/n * 100))
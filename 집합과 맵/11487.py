import sys

input = sys.stdin.readline

S = list(input().strip())

end = len(S)
result = []

for start in range(end):
    path = ""
    for left in range(start, end):
        path += S[left]
        result.append(path)

print(len(set(result)))
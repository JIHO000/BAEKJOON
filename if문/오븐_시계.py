A, B = map(int, input().split())
C = int(input())
A += (B+C) // 60
A %= 24
B = (B+C) % 60
print(A, B)

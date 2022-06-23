A, B, C = map(int, input().split())
if A == B == C:
    print(10000 + A * 1000)
elif A != B != C != A:
    print(max(A, B, C)*100)
else:
    print(1000 + ((A == B) | (A == C)) * A * 100 + (B == C) * B * 100)

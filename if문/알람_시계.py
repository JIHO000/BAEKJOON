H, M = map(int, input().split())
if M < 45 :
    H -= 1
H %= 24
M -= 45
M %= 60
print(H, M)

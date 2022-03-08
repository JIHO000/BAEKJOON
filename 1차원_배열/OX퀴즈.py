n = int(input())
for i in range(n):
    cnt = 0 
    score = 0
    data = list(input())
    for j in range(len(data)):
        if data[j] == "O":
            cnt += 1
            score += cnt
        else:
            cnt = 0
    print(score)
            
    
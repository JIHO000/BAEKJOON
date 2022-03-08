import time
start = time.time()  # 시작 시간 저장

A, B = map(int,input().split())
#while A != B != 0 != A:
while A != 0 != B:
    print(A+B)
    A, B = map(int,input().split())
    
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
import sys
import time
start = time.time()  # 시작 시간 저장
 
N, X = map(int, input().split())
# 작업 코드
#data = list(map(int, sys.stdin.readline().split()))
data = list(map(int, input().split()))
for i in [num for num in data if num < X]:
    print(i)
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
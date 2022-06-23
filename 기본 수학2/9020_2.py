from sys import stdin

def Goldbach():
    prime_check = [False, False] + [True] * 10000 # 소수면 False, 아니라면 True

    for i in range(2, 101): # 2 ~ 101까지 구하고, 이 수의 배수에 속하지 않으면 소수이다.
        if prime_check[i]: # 해당 수가 True라면 -> 소수가 체크가 되지 않았거나, 소수가 아니다
            for j in range(i + i, 10001, i): # 3 이상의 수부터 배수인 수를 체크
                prime_check[j] = False

    T = int(stdin.readline()) # 케이스 입력받기

    for _ in range(T):
        n = int(stdin.readline())

        A = n // 2 # A의 반부터 체크
        B = A # A와 같음

        for _ in range(10000): # 10000개 체크하여
            if prime_check[A] and prime_check[B]: # A와 B가 모두 소수라면?
                print(A, B) # 출력
                break
            A -= 1 # 두 수가 소수가 아니라면 A는 1을 빼주고
            B += 1 # B는 1을 더해준다.

Goldbach()
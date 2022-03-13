N = int(input())
bag = 0
while N >= 0 :
    if N % 5 == 0:
        print(N//5 + bag)
        break
    N -= 3
    bag += 1
else:
    print('-1')
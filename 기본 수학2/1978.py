N = int(input())
M = int(input())
demical_list=[]

for i in range(N,M + 1):
    if i != 1:
        for j in range(2, int(i**.5)+1):
            if i % j == 0:
                break
        else:
            demical_list.append(i)
if demical_list:
    print(sum(demical_list))
    print(demical_list[0])
else: 
    print(-1)
    
num = input()
nums = list(map(int, num))
nums.sort(reverse=True)

for i in nums:
    print(i, end = "")
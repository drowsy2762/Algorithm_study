# https://www.acmicpc.net/problem/1515 : 수 이어 쓰기 (python3)
# 2023-10-11

nums = input()
i = 0
while True:
    i += 1
    num = str(i)
    while len(num) > 0 and len(nums) > 0:
        if num[0] == nums[0]:
            nums = nums[1:]
        num = num[1:]
    if nums == "":
        print(i)
        break

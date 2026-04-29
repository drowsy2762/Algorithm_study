# https://www.acmicpc.net/problem/2621 : 카드게임 (python3)
# starttime : 2023-06-23 12:20 / endtime :
# inputtime 최적화
from sys import stdin


card = [list(input().split()) for _ in range(5)]
colors = [i[0] for i in card]
numbers = [int(i[1]) for i in card]
cnt_color = {"R": 0, "B": 0, "Y": 0, "G": 0}
cnt_num = [0 for _ in range(11)]
for i in range(5):
    color, number = card[i][0], int(card[i][1])
    cnt_color[color] += 1
    cnt_num[number] += 1

# 1번 규칙
sort_nums = numbers.copy()
sort_nums.sort()
if (
    5 in cnt_color.values()
    and sort_nums[0] + 1 == sort_nums[1]
    and sort_nums[1] + 1 == sort_nums[2]
    and sort_nums[2] + 1 == sort_nums[3]
    and sort_nums[3] + 1 == sort_nums[4]
):
    score = max(numbers) + 900
# 2번 규칙
elif 4 in cnt_num:
    score = cnt_num.index(4) + 800
# 3번 규칙
elif 3 in cnt_num and 2 in cnt_num:
    score = cnt_num.index(3) * 10 + cnt_num.index(2) + 700
# 4번 규칙
elif 5 in cnt_color.values():
    score = max(numbers) + 600
# 5번 규칙
elif (
    sort_nums[0] + 1 == sort_nums[1]
    and sort_nums[1] + 1 == sort_nums[2]
    and sort_nums[2] + 1 == sort_nums[3]
    and sort_nums[3] + 1 == sort_nums[4]
):
    score = max(numbers) + 500
# 6번 규칙
elif 3 in cnt_num:
    score = cnt_num.index(3) + 400
# 7번 규칙
elif 2 in cnt_num:
    first = cnt_num.index(2)
    num1 = numbers.copy()
    for i in num1:
        if i == first:
            numbers.remove(i)
    cnt_num[first] = 0
    if 2 in cnt_num:  # 7
        second = cnt_num.index(2)
        score = max(first, second) * 10 + min(first, second) + 300
    else:  # 8번 규칙
        score = first + 200
# 9번 규칙
else:
    score = max(numbers) + 100

print(score)

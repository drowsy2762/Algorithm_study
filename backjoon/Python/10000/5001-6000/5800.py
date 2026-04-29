k = int(input())
for i in range(k):
    math = list(map(int, input().split()))
    print("Class", i + 1)
    del math[0]
    gap = 0
    math.sort(reverse=True)
    for i in range(len(math)):
        gap = max(gap, math[i - 1] - math[i])
    print(
        "Max ",
        max(math),
        ", ",
        "Min ",
        min(math),
        ", ",
        "Largest gap ",
        gap,
        sep="",
    )

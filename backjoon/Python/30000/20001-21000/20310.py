# https://www.acmicpc.net/problem/20310 : 타노스 (python3)
# 2023-11-01


n = list(input())
zero = n.count("0") // 2
one = n.count("1") // 2

for _ in range(zero):
    n.pop(-(n[::-1].index("0")) - 1)
    print(-(n[::-1].index("0")) - 1, "t")

for _ in range(one):
    n.pop(n.index("1"))
    print(n.index("1"), "k")

print("".join(n))

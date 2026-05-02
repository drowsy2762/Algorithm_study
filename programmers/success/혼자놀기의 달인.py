# 2026-05-02


def solution(cards):
    n = len(cards)
    visited = [False] * n
    group_sizes = []

    for i in range(n):
        if visited[i]:
            continue

        cnt = 0
        cur = i

        while not visited[cur]:
            visited[cur] = True
            cur = cards[cur] - 1
            cnt += 1

        group_sizes.append(cnt)

    if len(group_sizes) < 2:
        return 0

    group_sizes.sort(reverse=True)
    return group_sizes[0] * group_sizes[1]


if __name__ == "__main__":
    solution()

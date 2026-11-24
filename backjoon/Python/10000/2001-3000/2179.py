# https://www.acmicpc.net/problem/2179 : 비슷한 단어 (python3)
# 2024-03-05
# 2026-11-24
import sys

input = sys.stdin.readline


def lcp_len(a: str, b: str) -> int:
    limit = min(len(a), len(b))
    cnt = 0
    for i in range(limit):
        if a[i] == b[i]:
            cnt += 1
        else:
            break
    return cnt


def solve():
    n = int(input().strip())
    words = [input().strip() for _ in range(n)]

    sorted_words = sorted(words)
    max_len = 0
    for i in range(n - 1):
        cur_len = lcp_len(sorted_words[i], sorted_words[i + 1])
        if cur_len > max_len:
            max_len = cur_len

    prefix_indices: dict[str, list[int]] = {}
    for idx, w in enumerate(words):
        if len(w) >= max_len:
            p = w[:max_len]
            if p not in prefix_indices:
                prefix_indices[p] = []
            prefix_indices[p].append(idx)

    best_pair: tuple[int, int] | None = None
    for idxs in prefix_indices.values():
        if len(idxs) >= 2:
            cand = (idxs[0], idxs[1])
            if best_pair is None or cand < best_pair:
                best_pair = cand

    if best_pair is not None:
        i, j = best_pair
        print(words[i])
        print(words[j])


if __name__ == "__main__":
    solve()

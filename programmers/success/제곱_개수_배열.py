# 2026-11-04
from bisect import bisect_right


def solution(arr, l, r):
    n = len(arr)

    pref_len = [0] * (n + 1)
    pref_sum = [0] * (n + 1)

    for idx, x in enumerate(arr):
        pref_len[idx + 1] = pref_len[idx] + x
        pref_sum[idx + 1] = pref_sum[idx] + (x * x)

    total_len = pref_len[n]

    def get_prefix_sum(count):
        if count <= 0:
            return 0
        block_idx = bisect_right(pref_len, count) - 1
        if block_idx >= n:
            return pref_sum[n]
        rem = count - pref_len[block_idx]
        return pref_sum[block_idx] + rem * arr[block_idx]

    K = get_prefix_sum(r) - get_prefix_sum(l - 1)
    window_len = r - l + 1
    curr_sum = get_prefix_sum(window_len)
    C = 1 if curr_sum == K else 0
    s = 0
    e = window_len
    i = 0
    j = bisect_right(pref_len, e) - 1

    while e < total_len:
        rem_left = pref_len[i + 1] - s
        rem_right = pref_len[j + 1] - e
        steps = rem_left if rem_left < rem_right else rem_right

        diff = arr[j] - arr[i]

        if diff == 0:
            if curr_sum == K:
                C += steps
        else:
            needed = K - curr_sum
            if needed % diff == 0:
                t = needed // diff
                if 1 <= t <= steps:
                    C += 1

        curr_sum += steps * diff
        s += steps
        e += steps

        if s == pref_len[i + 1]:
            i += 1
        if e == pref_len[j + 1]:
            j += 1

    return [K, C]

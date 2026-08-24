# 2026-08-24


def solution(s):
    if len(s) == 1:
        return 1

    min_compressed_len = len(s)
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]
        count = 1
        for i in range(step, len(s), step):
            current = s[i : i + step]
            if prev == current:
                count += 1
            else:
                compressed += (str(count) + prev) if count > 1 else prev
                prev = current
                count = 1

        compressed += (str(count) + prev) if count > 1 else prev

        min_compressed_len = min(min_compressed_len, len(compressed))

    return min_compressed_len

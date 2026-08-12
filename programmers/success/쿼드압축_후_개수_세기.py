# 2026-08-12


def solution(arr):
    answer = [0, 0]

    def compress(r, c, size):
        first_val = arr[r][c]
        is_same = True

        for i in range(r, r + size):
            for j in range(c, c + size):
                if arr[i][j] != first_val:
                    is_same = False
                    break
            if not is_same:
                break

        if is_same:
            answer[first_val] += 1
            return

        half = size // 2
        compress(r, c, half)
        compress(r, c + half, half)
        compress(r + half, c, half)
        compress(r + half, c + half, half)

    compress(0, 0, len(arr))

    return answer

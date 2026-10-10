# 2026-10-10
def solution(arr1, arr2):
    r1 = len(arr1)
    c2 = len(arr2[0])
    k_len = len(arr2)
    result = [[0] * c2 for _ in range(r1)]

    for i in range(r1):
        for j in range(c2):
            sum_val = 0
            for k in range(k_len):
                sum_val += arr1[i][k] * arr2[k][j]
            result[i][j] = sum_val

    return result

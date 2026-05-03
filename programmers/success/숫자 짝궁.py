from collections import Counter


def solution(X, Y):
    count_x = Counter(X)
    count_y = Counter(Y)

    result_list = []

    for i in range(9, -1, -1):
        char = str(i)
        common_count = min(count_x[char], count_y[char])

        result_list.append(char * common_count)

    result = "".join(result_list)

    if not result:
        return "-1"

    if result[0] == "0":
        return "0"

    return result

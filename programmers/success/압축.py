# 2026-09-24


def solution(msg):
    dictionary = {chr(ord("A") + i): i + 1 for i in range(26)}
    next_index = 27
    answer = []
    start = 0
    n = len(msg)

    while start < n:
        end = start + 1
        while end <= n and msg[start:end] in dictionary:
            end += 1
        w = msg[start : end - 1]
        answer.append(dictionary[w])

        if end <= n:
            w_plus_c = msg[start:end]
            dictionary[w_plus_c] = next_index
            next_index += 1
        start = end - 1

    return answer


# 검증용 테스트 코드
if __name__ == "__main__":
    test1 = "KAKAO"
    print("KAKAO 압축 결과:", solution(test1))
    # 기댓값: [11, 1, 27, 15]

    test2 = "TOBEORNOTTOBEORTOBEORNOT"
    print("TOBEORNOT... 결과:", solution(test2))
    # 기댓값: [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]

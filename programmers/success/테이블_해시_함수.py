def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key=lambda x: (x[col - 1], -x[0]))
    for i in range(row_begin, row_end + 1):
        current_row = data[i - 1]
        s_i = sum(val % i for val in current_row)
        answer ^= s_i
    return answer


"""
데이터베이스의 한 테이블은 모두 정수타입인 컬럼들로 구성됨
테이블은 2차원 행렬로 표현할 수 있으며 열 -> 컬럼 행 -> 튜플
모든 튜플에 대해 그 값이 중복되지 않도록 보장
"""

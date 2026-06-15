# 2026-06-15


def solution(plans):
    new_plans = []
    for name, start, playtime in plans:
        m_time = int(start[:2]) * 60 + int(start[3:])
        new_plans.append([name, m_time, int(playtime)])

    new_plans.sort(key=lambda x: x[1])
    answer = []
    stack = []

    for i in range(len(new_plans) - 1):
        curr_name, curr_start, curr_play = new_plans[i]
        next_name, next_start, _ = new_plans[i + 1]

        available_time = next_start - curr_start

        if curr_play <= available_time:
            answer.append(curr_name)
            available_time -= curr_play

            while stack and available_time > 0:
                prev_name, prev_remain = stack.pop()

                if prev_remain <= available_time:
                    answer.append(prev_name)
                    available_time -= prev_remain
                else:
                    stack.append([prev_name, prev_remain - available_time])
                    available_time = 0
        else:
            stack.append([curr_name, curr_play - available_time])

    answer.append(new_plans[-1][0])

    while stack:
        answer.append(stack.pop()[0])

    return answer


"""
컴퓨터 스케줄링 기법과 비슷함
one cpu -> FIFO는 아니고 LIFO아니고
새로운입력값이 들어오면 무조건 중지 후 새로운 요청으로 교체 
과제를 끝낸 시점에 새로운 과제가 생기면 그 과제를 진행
멈춰둔 과제가 여러개일 경우 가장 최근에 멈춘 과제부터 시작
=> FILO 기법 인데 중간에 추가하는루틴을 더한
"""

# 2026-05-04


def solution(record):
    answer = []
    user_dict = {}

    for r in record:
        parts = r.split()
        command = parts[0]
        uid = parts[1]

        if command in ("Enter", "Change"):
            nickname = parts[2]
            user_dict[uid] = nickname

    for r in record:
        parts = r.split()
        command = parts[0]
        uid = parts[1]

        final_nickname = user_dict[uid]

        if command == "Enter":
            answer.append(f"{final_nickname}님이 들어왔습니다.")
        elif command == "Leave":
            answer.append(f"{final_nickname}님이 나갔습니다.")

    return answer

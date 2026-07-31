# 2026-07-31


def solution(word):
    vowels = ["A", "E", "I", "O", "U"]
    cnt = 0
    answer = 0

    def dfs(current_word):
        nonlocal cnt, answer
        if current_word == word:
            answer = cnt
            return
        if len(current_word) == 5:
            return

        for v in vowels:
            cnt += 1
            dfs(current_word + v)
            if answer != 0:
                return

    dfs("")
    return answer

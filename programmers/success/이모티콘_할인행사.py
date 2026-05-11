# 2026-05-11


def solution(users, emoticons):
    answer = [0, 0]
    rates = [10, 20, 30, 40]
    m = len(emoticons)

    def dfs(idx, current_rates):
        nonlocal answer
        if idx == m:
            plus_cnt = 0
            sales_total = 0

            for sale_std, limit in users:
                user_spend = 0
                for i in range(m):
                    if current_rates[i] >= sale_std:
                        user_spend += emoticons[i] * (100 - current_rates[i]) // 100

                if user_spend >= limit:
                    plus_cnt += 1
                else:
                    sales_total += user_spend

            if plus_cnt > answer[0]:
                answer = [plus_cnt, sales_total]
            elif plus_cnt == answer[0] and sales_total > answer[1]:
                answer = [plus_cnt, sales_total]
            return

        for r in rates:
            current_rates.append(r)
            dfs(idx + 1, current_rates)
            current_rates.pop()

    dfs(0, [])

    return answer

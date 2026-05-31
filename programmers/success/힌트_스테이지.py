# 2026-05-31


def solution(cost, hint):
    n = len(cost)
    min_total_cost = float("inf")
    tickets = [0] * n

    def dfs(stage, current_cost):
        nonlocal min_total_cost
        if current_cost >= min_total_cost:
            return

        usable_tickets = min(tickets[stage], n - 1, len(cost[stage]) - 1)
        clear_cost = cost[stage][usable_tickets]

        if stage == n - 1:
            min_total_cost = min(min_total_cost, current_cost + clear_cost)
            return

        dfs(stage + 1, current_cost + clear_cost)
        bundle_price = hint[stage][0]

        for t in hint[stage][1:]:
            tickets[t - 1] += 1

        dfs(stage + 1, current_cost + clear_cost + bundle_price)

        for t in hint[stage][1:]:
            tickets[t - 1] -= 1

    dfs(0, 0)

    return min_total_cost

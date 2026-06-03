# 2026-06-03


def solution(players, m, k):
    answer = 0
    server_logs = [0] * 24

    for t in range(24):
        active_servers = 0
        start_time = max(0, t - k + 1)
        for i in range(start_time, t):
            active_servers += server_logs[i]

        required_servers = players[t] // m
        if required_servers > active_servers:
            needed = required_servers - active_servers
            server_logs[t] = needed
            answer += needed

    return answer

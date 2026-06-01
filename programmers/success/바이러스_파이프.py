# 2026-06-01

from collections import deque


def solution(n, infection, edges, k):
    tree = [[] for _ in range(n + 1)]
    for x, y, p in edges:
        tree[x].append((y, p))
        tree[y].append((x, p))

    memo = {}

    def spread(infected, p):
        new_infected = set(infected)
        q = deque(infected)
        while q:
            node = q.popleft()
            for n, e in tree[node]:
                if e == p and n not in new_infected:
                    new_infected.add(n)
                    q.append(n)

        return new_infected

    def dfs(infected, current_k):
        state = (frozenset(infected), current_k)
        if state in memo:
            return memo[state]
        if current_k == 0:
            return len(infected)

        best = len(infected)
        for p in [1, 2, 3]:
            new_infected = spread(infected, p)
            result = dfs(new_infected, current_k - 1)
            best = max(best, result)

        memo[state] = best

        return best

    initial_infected = {infection} if isinstance(infection, int) else set(infection)
    answer = dfs(initial_infected, k)
    return answer

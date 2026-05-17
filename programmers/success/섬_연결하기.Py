# 2026-05-17


def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    parent = [i for i in range(n)]
    answer = 0

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        rootA = find(a)
        rootB = find(b)
        if rootA < rootB:
            parent[rootB] = rootA
        else:
            parent[rootA] = rootB

    for a, b, cost in costs:
        if find(a) != find(b):
            union(a, b)
            answer += cost

    return answer

# 2026-05-10


def solution(n, wires):
    tree = [[] for _ in range(n + 1)]
    for i, j in wires:
        tree[i].append(j)
        tree[j].append(i)

    def dfs(start, ignore_a, ignore_b):
        visited = [False] * (n + 1)
        visited[start] = True
        stack = [start]
        count = 1

        while stack:
            curr = stack.pop()
            for next_node in tree[curr]:
                if (curr == ignore_a and next_node == ignore_b) or (
                    curr == ignore_b and next_node == ignore_a
                ):
                    continue

                if not visited[next_node]:
                    visited[next_node] = True
                    stack.append(next_node)
                    count += 1

        return count

    answer = float("inf")

    for a, b in wires:
        count_a = dfs(a, a, b)
        count_b = n - count_a
        diff = abs(count_a - count_b)
        answer = min(answer, diff)

    return answer

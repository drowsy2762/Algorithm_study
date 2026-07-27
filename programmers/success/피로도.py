def solution(k, dungeons):
    n = len(dungeons)
    visited = [False] * n

    def dfs(fatigue, cnt):
        local_max = cnt
        for i in range(n):
            min_fatigue = dungeons[i][0]
            consume = dungeons[i][1]
            if not visited[i] and fatigue >= min_fatigue:
                visited[i] = True
                result = dfs(fatigue - consume, cnt + 1)
                local_max = max(local_max, result)
                visited[i] = False

        return local_max

    return dfs(k, 0)

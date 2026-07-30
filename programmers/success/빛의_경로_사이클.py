# 2026-07-30


def solution(grid):
    answer = []
    R = len(grid)
    C = len(grid[0])
    visited = [[[False] * 4 for _ in range(C)] for _ in range(R)]

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    for r in range(R):
        for c in range(C):
            for d in range(4):
                if visited[r][c][d]:
                    continue
                count = 0
                curr_r, curr_c, curr_d = r, c, d

                while not visited[curr_r][curr_c][curr_d]:
                    visited[curr_r][curr_c][curr_d] = True
                    count += 1

                    cell = grid[curr_r][curr_c]
                    if cell == "L":
                        curr_d = (curr_d - 1) % 4
                    elif cell == "R":
                        curr_d = (curr_d + 1) % 4
                    curr_r = (curr_r + dr[curr_d]) % R
                    curr_c = (curr_c + dc[curr_d]) % C

                answer.append(count)

    return sorted(answer)

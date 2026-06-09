# 2026-06-09


def solution(edges):
    in_degree = {}
    out_degree = {}
    vertices = set()

    for u, v in edges:
        vertices.add(u)
        vertices.add(v)
        out_degree[u] = out_degree.get(u, 0) + 1
        in_degree[v] = in_degree.get(v, 0) + 1

    created_vertex = 0
    donut_cnt = 0
    bar_cnt = 0
    eight_cnt = 0

    for v in vertices:
        out_d = out_degree.get(v, 0)
        in_d = in_degree.get(v, 0)
        if in_d == 0 and out_d >= 2:
            created_vertex = v
            break

    total_graphs = out_degree.get(created_vertex, 0)

    for v in vertices:
        if v == created_vertex:
            continue

        out_d = out_degree.get(v, 0)
        if out_d == 0:
            bar_cnt += 1
        elif out_d == 2:
            eight_cnt += 1

    donut_cnt = total_graphs - bar_cnt - eight_cnt

    return [created_vertex, donut_cnt, bar_cnt, eight_cnt]

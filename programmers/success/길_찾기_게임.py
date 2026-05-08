# 2026-05-08


import sys

sys.setrecursionlimit(10**6)


def solution(nodeinfo):
    nodes = [[x, y, i + 1] for i, (x, y) in enumerate(nodeinfo)]
    nodes.sort(key=lambda v: (-v[1], v[0]))

    pre_result = []
    post_result = []

    def traverse(current_nodes):
        if not current_nodes:
            return
        root = current_nodes[0]
        root_x = root[0]
        root_id = root[2]

        pre_result.append(root_id)
        left_nodes = [node for node in current_nodes[1:] if node[0] < root_x]
        right_nodes = [node for node in current_nodes[1:] if node[0] > root_x]

        traverse(left_nodes)
        traverse(right_nodes)
        post_result.append(root_id)

    traverse(nodes)

    return [pre_result, post_result]

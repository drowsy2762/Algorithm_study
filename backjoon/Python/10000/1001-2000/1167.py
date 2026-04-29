# https://www.acmicpc.net/problem/1167
# 2026-04-11
import sys
from collections import deque

def solution():
    input = sys.stdin.readline

    V = int(input())
    tree = [[] for _ in range(V + 1)]
    for _ in range(V):
        line = list(map(int, input().split()))
        u = line[0]
        for i in range(1, len(line) - 1, 2):
            tree[u].append((line[i], line[i+1]))

    def BFS(start):
        visited = [-1] * (V + 1)
        q = deque([start])
        visited[start] = 0
        max_dist = 0
        farthest_node = start
        
        while q:
            curr = q.popleft()
            for adj_node, weight in tree[curr]:
                if visited[adj_node] == -1:
                    visited[adj_node] = visited[curr] + weight
                    q.append(adj_node)
                    if visited[adj_node] > max_dist:
                        max_dist = visited[adj_node]
                        farthest_node = adj_node
        return farthest_node, max_dist
    
    point, _ = BFS(1)
    _, diameter = BFS(point)
    
    print(diameter)

if __name__ == "__main__":
    solution()
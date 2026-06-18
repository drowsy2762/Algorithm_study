INF = 10**15


class Node:
    def __init__(self, u, v, delay, safety):
        self.u = u
        self.v = v
        self.delay = delay
        self.safety = safety


class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]

    def addEdge(self, u, v, delay, safety):
        self.adj[u].append(Node(u, v, delay, safety))
        self.adj[v].append(Node(v, u, delay, safety))

    def isConnected(self, u, v):
        for edge in self.adj[u]:
            if edge.v == v:
                return True
        return False


class PriorityQueue:
    def __init__(self, n):
        self.heap = []

    def add(self, item):
        self.heap.append(item)
        idx = len(self.heap) - 1
        while idx > 0:
            parent = (idx - 1) // 2
            if self.heap[idx][0] < self.heap[parent][0]:
                self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
                idx = parent
            else:
                break

    def remove_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        min_item = self.heap[0]
        self.heap[0] = self.heap.pop()

        idx = 0
        size = len(self.heap)
        while 2 * idx + 1 < size:
            left = 2 * idx + 1
            right = 2 * idx + 2
            smallest = left

            if right < size and self.heap[right][0] < self.heap[left][0]:
                smallest = right

            if self.heap[idx][0] > self.heap[smallest][0]:
                self.heap[idx], self.heap[smallest] = (
                    self.heap[smallest],
                    self.heap[idx],
                )
                idx = smallest
            else:
                break

        return min_item


def dijkstra(graph, n, M, K, P, source=1):
    dist = [INF] * n
    dist[source] = 0
    pq = PriorityQueue(n)
    pq.add((0, source))

    while pq.heap:
        current_dist, u = pq.remove_min()
        if current_dist > dist[u]:
            continue

        for edge in graph.adj[u]:
            v = edge.v
            cost = edge.delay
            if edge.safety < K:
                cost += P
            if dist[u] + cost < dist[v]:
                dist[v] = dist[u] + cost
                pq.add((dist[v], v))

    return dist


def main():
    N = 5
    M = 8
    K = 2
    P = 10

    graph = Graph(N)
    graph.addEdge(0, 1, 10, 3)
    graph.addEdge(0, 2, 6, 1)
    graph.addEdge(0, 3, 5, 2)
    graph.addEdge(1, 2, 3, 2)
    graph.addEdge(1, 3, 15, 2)
    graph.addEdge(2, 3, 4, 2)
    graph.addEdge(2, 4, 8, 3)
    graph.addEdge(3, 4, 9, 1)

    dist = dijkstra(graph, N, M, K, P, source=1)

    for i in range(N):
        if dist[i] == INF:
            print(f"1 → {i}: 도달 불가")
        else:
            print(f"1 → {i}: {dist[i]}")


if __name__ == "__main__":
    main()

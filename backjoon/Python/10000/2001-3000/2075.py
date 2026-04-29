# https://www.acmicpc.net/problem/2075 : N번째 큰수 (python3)
# 2023-11-13
from sys import stdin
import heapq

input = stdin.readline

n = int(input())
heap = []
for _ in range(n):
    numbers = map(int, input().split())
    for number in numbers:
        if len(heap) < n:
            heapq.heappush(heap, number)
        else:
            if heap[0] < number:
                heapq.heappop(heap)
                heapq.heappush(heap, number)
print(heap[0])

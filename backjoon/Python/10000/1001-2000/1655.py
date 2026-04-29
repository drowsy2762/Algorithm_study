# 가운데를 말해요 : https://www.acmicpc.net/problem/1655 (python3)

# 순서대로 들어오는 수들을 배열로 나눠서 넣음
#

import sys
import heapq

n = int(sys.stdin.readline())
max_heap = []
min_heap = []

for _ in range(n):
    num = int(sys.stdin.readline())
    # max_heap과 min_heap의 길이가 같다면 max_heap에 넣어줌
    # max_heap에는 음수로 넣어줌으로써 최대힙을 구현
    # min_heap에는 양수로 넣어줌으로써 최소힙을 구현
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, (-num, num))
    else:
        heapq.heappush(min_heap, (num, num))

    # max_heap의 최대값이 min_heap의 최소값보다 크다면
    # max_heap의 최대값과 min_heap의 최소값을 바꿔줌
    if min_heap and max_heap[0][1] > min_heap[0][1]:
        max_value = heapq.heappop(max_heap)[1]
        min_value = heapq.heappop(min_heap)[1]
        heapq.heappush(max_heap, (-min_value, min_value))
        heapq.heappush(min_heap, (max_value, max_value))
    # max_heap의 최대값을 출력
    print(max_heap[0][1])

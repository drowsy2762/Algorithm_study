# 2026-07-02


from heapq import heappop, heappush


def solution(n, k, enemy):
    if k >= len(enemy):
        return len(enemy)
    heap = []
    for i in range(k):
        heappush(heap, enemy[i])

    for i in range(k, len(enemy)):
        heappush(heap, enemy[i])
        smallest = heappop(heap)
        n -= smallest

        if n < 0:
            return i

    return len(enemy)


"""
병사 n명, 적의 공격을 순서대로 막음
enemy[i] 마리 등장
교환비 1 : 1
라운드 스킵비용 무적권 k => cnt / 무적권을 최대한 잘 사용하고자함 >> 
dp문제 -> 
"""

# 2026-08-18


def solution(s):
    parsed_chunks = s[2:-2].split("},{")
    subsets = [list(map(int, chunk.split(","))) for chunk in parsed_chunks]
    subsets.sort(key=len)

    answer = []
    visited = set()

    for subset in subsets:
        for num in subset:
            if num not in visited:
                answer.append(num)
                visited.add(num)

    return answer

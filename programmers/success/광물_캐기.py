# 2026-06-16


def solution(picks, minerals):
    total_picks = sum(picks)
    minerals = minerals[: total_picks * 5]
    chunks = []
    for i in range(0, len(minerals), 5):
        chunk = minerals[i : i + 5]
        dia = chunk.count("diamond")
        iron = chunk.count("iron")
        stone = chunk.count("stone")
        chunks.append((dia, iron, stone))

    chunks.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)
    answer = 0
    dia_p, iron_p, stone_p = picks
    for dia, iron, stone in chunks:
        if dia_p > 0:
            answer += dia + iron + stone
            dia_p -= 1
        elif iron_p > 0:
            answer += dia * 5 + iron * 1 + stone * 1
            iron_p -= 1
        elif stone_p > 0:
            answer += dia * 25 + iron * 5 + stone * 1
            stone_p -= 1

    return answer

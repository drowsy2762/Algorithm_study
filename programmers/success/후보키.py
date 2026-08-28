# 2026-08-28


def solution(relation):
    row_len = len(relation)
    col_len = len(relation[0])

    def get_combinations(elements, r):
        results = []

        def backtrack(start, current_comb):
            if len(current_comb) == r:
                results.append(tuple(current_comb))
                return
            for i in range(start, len(elements)):
                current_comb.append(elements[i])
                backtrack(i + 1, current_comb)
                current_comb.pop()

        backtrack(0, [])
        return results

    all_combinations = []
    col_indices = list(range(col_len))

    for size in range(1, col_len + 1):
        combs_of_size = get_combinations(col_indices, size)
        all_combinations.extend(combs_of_size)

    candidate_keys = []

    for comb in all_combinations:
        projected_rows = [tuple(row[c] for c in comb) for row in relation]
        if len(set(projected_rows)) == row_len:
            is_minimal = True
            for cand in candidate_keys:
                if set(cand).issubset(set(comb)):
                    is_minimal = False
                    break

            if is_minimal:
                candidate_keys.append(comb)

    return len(candidate_keys)

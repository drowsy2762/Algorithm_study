# 2026-08-26


def solution(skill, skill_trees):
    skill_set = set(skill)
    valid_count = 0
    for tree in skill_trees:
        skill_idx = 0
        is_valid = True
        for s in tree:
            if s in skill_set:
                if s == skill[skill_idx]:
                    skill_idx += 1
                else:
                    is_valid = False
                    break
        if is_valid:
            valid_count += 1
    return valid_count


# def solution(skill, skill_trees):
#     return sum(
#         skill.startswith("".join([s for s in tree if s in skill]))
#         for tree in skill_trees
#     )

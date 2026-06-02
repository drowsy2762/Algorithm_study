# 2026-06-02


def solution(dist_limit, split_limit):
    max_ans = 1
    for i in range(32):
        for j in range(21):

            if (2**i) * (3**j) <= split_limit:
                layers = [2] * i + [3] * j

                D = dist_limit
                W = 1

                for k in layers:
                    if D >= W:
                        D -= W
                        W *= k
                    else:
                        W = (W - D) + D * k
                        D = 0
                        break

                max_ans = max(max_ans, W)

    return max_ans

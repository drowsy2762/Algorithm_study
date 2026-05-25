# 2026-05-25
import sys

sys.setrecursionlimit = 300000


def solution(q, a):
    MOD = 998244353
    n = len(a)
    first_idx = {}
    last_idx = {}
    for i, v in enumerate(a):
        if v not in first_idx:
            first_idx[v] = i
        last_idx[v] = i

    stack = []
    for i, v in enumerate(a):
        while stack and stack[-1] > v:
            stack.pop()
        if v in first_idx and first_idx[v] != i:
            if not stack or stack[-1] != v:
                return 0
        stack.append(v)

    max_val_in_a = max(a)
    if max_val_in_a > q:
        return 0

    MAX_Q = max(q, 100005) + 5
    fact = [1] * MAX_Q
    inv = [1] * MAX_Q
    for i in range(1, MAX_Q):
        fact[i] = (fact[i - 1] * i) % MOD

    inv[MAX_Q - 1] = pow(fact[MAX_Q - 1], MOD - 2, MOD)
    for i in range(MAX_Q - 2, -1, -1):
        inv[i] = (inv[i + 1] * (i + 1)) % MOD

    def nCr(num, r):
        if r < 0 or r > num:
            return 0
        return fact[num] * inv[r] % MOD * inv[num - r] % MOD

    def nHr(num, r):
        if num == 0 and r == 0:
            return 1
        return nCr(num + r - 1, r)

    val_indices = {}
    for i, v in enumerate(a):
        if v not in val_indices:
            val_indices[v] = []
        val_indices[v].append(i)
    unique_vals = sorted(list(set(a)))

    def solve(l, r, val_idx):
        if l > r:
            current_v = unique_vals[val_idx - 1] if val_idx > 0 else 0
            return nHr(1, q - current_v)

        if val_idx >= len(unique_vals):
            current_v = unique_vals[val_idx - 1] if val_idx > 0 else 0
            return nHr(r - l + 2, q - current_v)

        target_v = unique_vals[val_idx]
        indices = [i for i in val_indices[target_v] if l <= i <= r]

        if not indices:
            return solve(l, r, val_idx + 1)

        res_ways = 1
        res_ways = (res_ways * solve(l, indices[0] - 1, val_idx + 1)) % MOD
        for i in range(len(indices) - 1):
            res_ways = (
                res_ways * solve(indices[i] + 1, indices[i + 1] - 1, val_idx + 1)
            ) % MOD
        res_ways = (res_ways * solve(indices[-1] + 1, r, val_idx + 1)) % MOD
        prev_v = unique_vals[val_idx - 1] if val_idx > 0 else 0
        missing_count = (target_v - prev_v) - 1

        if missing_count > 0:
            slots = len(indices) + 1
            res_ways = (res_ways * nHr(slots, missing_count)) % MOD

        return res_ways

    return solve(0, n - 1, 0) % MOD

#!/usr/bin/env python3
from collections import namedtuple

N, W = list(map(int, input().split()))
Item = namedtuple("Item", ["value", "weight"])
# DPとitemのインデックスを揃えるために、ダミーで1件入れておく
items = [(None, None)]
for _ in range(N):
    v, w = list(map(int, input().split()))
    items.append(Item(v, w))

dp = [[0] * (W + 1) for _ in range(N + 1)]

for i in range(N + 1):
    if i == 0:
        continue
    w = items[i].weight
    v = items[i].value

    for j in range(W + 1):
        if j - items[i].weight < 0:
            continue
        v_0 = dp[i - 1][j - w] + v
        v_1 = dp[i - 1][j]
        dp[i][j] = max(v_0, v_1)

ans = int(max(dp[N]))

print(ans)
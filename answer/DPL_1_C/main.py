#!/usr/bin/env python3
from collections import namedtuple

N, W = list(map(int, input().split()))
Item = namedtuple("Item", ["value", "weight"])

item_list = [None]  # 添字を揃えるためにダミーを1個いれる

for _ in range(N):
    v, w = list(map(int, input().split()))
    item_list.append(Item(v, w))

dp = [[0] * (W + 1) for _ in range(N + 1)]
max_value = 0
for i in range(1, N + 1):
    item = item_list[i]
    w = item.weight
    v = item.value
    for j in range(1, W + 1):
        # print(f"i-1={i-1}, {j=}")
        if j - w < 0:
            dp[i][j] = dp[i - 1][j]
            continue
        # 追加しなかった場合の価値
        value_0 = dp[i - 1][j]  # ↓の遷移
        # 追加した場合の価値
        value_1 = dp[i - 1][j - w] + v  # ↘︎の遷移
        value_2 = dp[i][j - w] + v  # →の遷移
        new_value = max([value_0, value_1, value_2])
        dp[i][j] = new_value
        max_value = max([max_value, new_value])

ans = max_value
print(ans)
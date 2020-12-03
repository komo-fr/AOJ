#!/usr/bin/env python3

N = int(input().split()[0])
xy_list = []

for _ in range(N):
    X = input()
    Y = input()
    xy_list.append((X, Y))


def calc_max_lcs(X: str, Y: str) -> int:
    dp = []
    max_lcs = -float("inf")
    for j in range(len(Y) + 1):
        dp_row = []
        for i in range(len(X) + 1):
            if i == 0 or j == 0:
                lcs = 0
            else:
                if X[i - 1] == Y[j - 1]:
                    # 末尾が一致していたら左斜め上+1
                    lcs = dp[j - 1][i - 1] + 1
                else:
                    # 上と左
                    lcs = max([dp[j - 1][i], dp_row[i - 1]])
            dp_row.append(lcs)
            max_lcs = max([lcs, max_lcs])
        dp.append(dp_row)
    return max_lcs


for i in range(N):
    X, Y = xy_list[i]
    print(calc_max_lcs(X, Y))

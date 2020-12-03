#!/usr/bin/env python3

N = int(input().split()[0])


def calc_max_lcs(X: str, Y: str, dp) -> int:
    max_lcs = -float("inf")
    for j in range(len(Y) + 1):
        for i in range(len(X) + 1):
            if i == 0 or j == 0:
                lcs = 0
            else:
                if X[i - 1] == Y[j - 1]:
                    # 末尾が一致していたら左斜め上+1
                    lcs = dp[j - 1][i - 1] + 1
                else:
                    # 上と左
                    lcs = max([dp[j - 1][i], dp[j][i - 1]])
            dp[j][i] = lcs
            max_lcs = max([lcs, max_lcs])
    return max_lcs


for i in range(N):
    X = input()
    Y = input()
    dp_table = [[0] * (len(X) + 2) for _ in range(len(Y) + 2)]
    print(calc_max_lcs(X, Y, dp_table))

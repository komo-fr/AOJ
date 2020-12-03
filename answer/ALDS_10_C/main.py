#!/usr/bin/env python3


def calc_max_lcs(X: str, Y: str, dp) -> int:
    max_lcs = 0
    pre_row = dp[0]
    Y = " " + Y
    X = " " + X
    for j, YY in enumerate(Y):
        if j == 0:
            continue
        row = dp[j]
        for i, XX in enumerate(X):
            if i == 0:
                continue
            if XX == YY:
                # 末尾が一致していたら左斜め上+1
                pre_lcs = pre_row[i - 1]
                row[i] = pre_lcs + 1
                if pre_lcs + 1 > max_lcs:
                    max_lcs = pre_lcs + 1
            else:
                # 上と左
                top, left = pre_row[i], row[i - 1]
                if top > left:
                    row[i] = top
                else:
                    row[i] = left
        pre_row = row
    return max_lcs


if __name__ == "__main__":

    N = int(input().split()[0])
    for i in range(N):
        X = input()
        Y = input()
        dp_table = [[0] * (len(X) + 2) for _ in range(len(Y) + 2)]

        print(calc_max_lcs(X, Y, dp_table))

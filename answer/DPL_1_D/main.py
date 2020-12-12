#!/usr/bin/env python3
import bisect

N = int(input().split()[0])
a_list = []

for _ in range(N):
    a = int(input().split()[0])
    a_list.append(a)

dp = [float("inf") for i in range(N)]
max_len = 1

for j, a in enumerate(a_list):
    if j == 0:
        dp[0] = a
        continue
    i = bisect.bisect_right(dp, a)
    # print(f"{i=}, {a=}, {dp=}")
    if i == 0 or (i != 0 and a != dp[i - 1]):
        dp[i] = min([a, dp[i]])
        max_len = max([max_len, i + 1])

# print(dp)
ans = max_len
print(ans)

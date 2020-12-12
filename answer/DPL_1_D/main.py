#!/usr/bin/env python3

N = int(input().split()[0])
a_list = []

for _ in range(N):
    a = int(input().split()[0])
    a_list.append(a)
dp = []
max_dp_v = 1
for i, a in enumerate(a_list):
    max_v = 1
    for j in range(i):
        if a_list[j] < a:
            max_v = max([max_v, dp[j] + 1])
    dp.append(max_v)
    max_dp_v = max([max_v, max_dp_v])
# print(dp)
ans = max_dp_v
print(ans)

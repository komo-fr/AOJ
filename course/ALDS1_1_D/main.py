#!/usr/bin/env python3

n = int(input().split()[0])
max_diff = -float("inf")
min_value = float("inf")

for i in range(n):
    r = int(input().split()[0])
    if i != 0:
        diff = r - min_value
        max_diff = max(max_diff, diff)
    min_value = min(min_value, r)

ans = max_diff
print(max_diff)

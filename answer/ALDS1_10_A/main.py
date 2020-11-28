#!/usr/bin/env python3

N = int(input().split()[0])
a_list = []
for i in range(N + 1):
    if i in [0, 1]:
        a_list.append(1)
        continue
    a_list.append(a_list[i - 1] + a_list[i - 2])

ans = a_list[-1]
print(ans)
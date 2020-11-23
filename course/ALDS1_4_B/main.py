#!/usr/bin/env python3
import bisect

n = int(input().split()[0])
s_list = list(map(int, input().split()))
q = int(input().split()[0])
t_list = list(map(int, input().split()))


def binary_search(target_list, x):
    # target_list内にxがあったらTrue, なかったらFalseを返す
    index = bisect.bisect_left(target_list, t)
    if index >= len(target_list):
        # 探索対象の値が最大になる場合
        index -= 1
    if target_list[index] == t:
        return True  # 見つかった
    else:
        return False


count = 0
for t in t_list:
    if binary_search(s_list, t):
        count += 1
print(count)
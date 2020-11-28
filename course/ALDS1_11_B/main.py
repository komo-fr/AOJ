#!/usr/bin/env python3
from collections import defaultdict
import sys

N = int(input().split()[0])

# 再起の上限を解除
sys.setrecursionlimit(N * 10)

# 隣接ノードの情報 key=node_id, value=隣接するノードのリスト
neighbor_dict = defaultdict(lambda: [])
# 探索済みのノード情報
# start: 行きで経由したときのステップ数（発見時刻）
# end: 帰りで経由したときのステップ数（完了時刻）
step_dict = defaultdict(lambda: {})

for _ in range(N):
    u, k, *v_list = list(map(int, input().split()))
    neighbor_dict[u] = v_list

# ステップ数
step = 0


def search(node_id):
    global step
    global step_dict
    step += 1
    neighbor_list = neighbor_dict[node_id]
    if not step_dict[node_id]:
        step_dict[node_id] = dict(start=step)

    for neighbor_id in neighbor_list:
        if step_dict[neighbor_id]:
            # 経由済の隣接ノードはスキップする
            continue
        search(neighbor_id)
    step += 1
    step_dict[node_id]["end"] = step


search(1)

for i in range(N):
    print(f"{i+1} {step_dict[i+1]['start']} {step_dict[i+1]['end']}")

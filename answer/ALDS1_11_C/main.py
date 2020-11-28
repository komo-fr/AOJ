#!/usr/bin/env python3
# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_11_C
from collections import defaultdict, deque
import sys

N = int(input().split()[0])

# 隣接ノードの情報 key=node_id, value=隣接するノードのリスト
neighbor_dict = defaultdict(lambda: [])

for _ in range(N):
    u, k, *v_list = list(map(int, input().split()))
    neighbor_dict[u] = v_list

# 探索済みのノード情報
# 1からの距離が入っている。1から到達できない場合は-1
step_dict = defaultdict(lambda: -1)

start_node_id = 1
step_dict[start_node_id] = 0
# 次の探索対象が入ったキュー
work_queue = deque([start_node_id])

while work_queue:
    # 今いるノード
    current_id = work_queue.popleft()
    for neighbor_id in neighbor_dict[current_id]:
        # 今いるノードに隣接するノードを巡回する
        if step_dict[neighbor_id] != -1:
            # 経由済のノードはスキップする
            # 今いるノードと同じ階層にいるノードは、
            # これの1つ前のステップで既に距離が更新されている=巡回済の扱いになっているのでスキップされる
            continue
        # 距離を更新（現在値 + 1）
        step_dict[neighbor_id] = step_dict[current_id] + 1
        # 次の巡回対象
        work_queue.append(neighbor_id)

for i in range(N):
    print(f"{i+1} {step_dict[i+1]}")

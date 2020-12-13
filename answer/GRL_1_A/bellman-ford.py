#!/usr/bin/env python3
from collections import namedtuple
from logging import debug, DEBUG, basicConfig

fmt = "%(levelname)s: %(message)s"
# basicConfig(level=DEBUG, format=fmt)

V, E, r = list(map(int, input().split()))
edge_list = []
Edge = namedtuple("Edge", ["start", "end", "cost"])
for _ in range(E):
    s, t, d = list(map(int, input().split()))
    edge_list.append(Edge(s, t, d))

# ベルマンフォード法
# 始点ノードrから各ノードへの距離リスト
d = [float("inf") for _ in range(V)]

d[r] = 0
while True:
    # 更新が発生したかどうか管理するフラグ
    is_update = False
    # debug("================================")
    for i, edge in enumerate(edge_list):

        # debug(f"edge_i={i}: {edge}")
        # debug(
        #     f"d[{edge.end}] > (d[{edge.start}] + edge.cost) 【{d[edge.end]} > ({d[edge.start]} + {edge.cost})】"
        # )

        # if d[edge.start] != float("inf") and d[edge.end] > (d[edge.start] + edge.cost):
        if d[edge.end] > (d[edge.start] + edge.cost):
            # d[edge.end]に直接行くより
            # d[edge.start]を経由した方が距離コストが小さい
            is_update = True
            d[edge.end] = d[edge.start] + edge.cost
            # debug("★★★★★★更新発生★★★★★★")

    # debug(f"{d=}")
    if not is_update:
        # 更新が止まったら終了
        break

for dd in d:
    dd = "INF" if dd == float("inf") else dd
    print(dd)

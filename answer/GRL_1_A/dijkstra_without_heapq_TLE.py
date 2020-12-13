#!/usr/bin/env python3
from collections import namedtuple, defaultdict
from logging import debug, DEBUG, basicConfig

fmt = "%(levelname)s: %(message)s"
# basicConfig(level=DEBUG, format=fmt)

V, E, r = list(map(int, input().split()))
edge_list = []
# 始点をキーとするエッジ辞書
edge_dict = defaultdict(lambda: [])
Edge = namedtuple("Edge", ["end", "cost"])
for _ in range(E):
    s, t, d = list(map(int, input().split()))
    edge_dict[s].append(Edge(t, d))

# ダイクストラ法（ヒープ無し）
# #27(08_large_00.in)で15.99sでTLEする
# #26(07_large_03.in)は1.26sでACするので
# バグによって無限ループになっている可能性もある
# 始点ノードrから各ノードへの距離リスト
d = [float("inf") for _ in range(V)]
d[r] = 0
# 距離が確定したかどうかのリスト
done_list = [False for _ in range(V)]
done_count = 0

while done_count != V:
    # 次の確定対象となるノードID
    # 現時点で距離が未確定のノードのうち、距離が最小になるものを確定する
    min_d_node_id = None
    for node_id in range(V):
        if not done_list[node_id]:
            # 未確定のノード
            if min_d_node_id is None or d[node_id] < d[min_d_node_id]:
                min_d_node_id = node_id
    if min_d_node_id is None:
        # 更新が発生しなかったら終了
        break

    done_count += 1
    # 距離が確定
    done_list[min_d_node_id] = True
    # min_d_node_idと隣接する他のノードの距離を更新する
    for edge in edge_dict[min_d_node_id]:
        neighbor_node_id = edge.end
        # min_d_node_idを経由する方が距離が縮まるなら更新する
        new_d = d[min_d_node_id] + edge.cost
        d[neighbor_node_id] = min([d[neighbor_node_id], new_d])


for dd in d:
    dd = "INF" if dd == float("inf") else dd
    print(dd)

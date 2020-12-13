#!/usr/bin/env python3
from collections import namedtuple, defaultdict
import heapq

# from logging import debug, DEBUG, basicConfig

# fmt = "%(levelname)s: %(message)s"
# basicConfig(level=DEBUG, format=fmt)

V, E, r = list(map(int, input().split()))
edge_list = []
# 始点をキーとするエッジ辞書
edge_dict = defaultdict(lambda: [])
Edge = namedtuple("Edge", ["end", "cost"])
for _ in range(E):
    s, t, d = list(map(int, input().split()))
    edge_dict[s].append(Edge(t, d))

# ダイクストラ法（ヒープ有り）
# 開始点ノードrから各ノードへの距離リスト
d = [float("inf") for _ in range(V)]
d[r] = 0
# 距離が確定したかどうかのリスト
Node = namedtuple("Node", ["d", "node_id"])
d_heapq = []
heapq.heappush(d_heapq, Node(0, r))
done_count = 0

while d_heapq:
    # 次の確定対象となるノードID
    # 現時点で距離が未確定のノードのうち、距離が最小になるものを確定する

    # 未確定のノードのうち、最小のものを取得する
    min_node = heapq.heappop(d_heapq)
    # print(f"{min_node=}")
    if d[min_node.node_id] < min_node.d:
        # 更新の必要なし
        continue

    # 更新が発生する
    # node_nodeと隣接する他のノードの距離を更新する
    for edge in edge_dict[min_node.node_id]:
        neighbor_node_id = edge.end
        # min_nodeを経由する方が距離が縮まるなら更新する
        new_d = d[min_node.node_id] + edge.cost
        if (d[min_node.node_id] + edge.cost) < d[neighbor_node_id]:
            new_d = d[min_node.node_id] + edge.cost
            d[neighbor_node_id] = new_d
            updated_node = Node(new_d, neighbor_node_id)
            heapq.heappush(d_heapq, updated_node)
    # print(d_heapq)

for dd in d:
    dd = "INF" if dd == float("inf") else dd
    print(dd)

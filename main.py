# 旅行商问题
# 设有n个城市，城市之间的距离已知。
# 某旅行者希望从某个城市出发旅行完其余所有的城市最后回到出发的城市。
# 要求除起始出发的城市之外，其余的城市只能经过一次，求整个旅行的最短距离。
import random

import networkx as nx
from matplotlib import pyplot as plt

input = input("输入城市数量，城市之间距离在10-100随机,n:")
n = int(input)
G = nx.DiGraph()

for i in range(1, n+1):
    for j in range(1, i + 1):
        if i != j:
            G.add_weighted_edges_from([(i, j, 1)])
nx.draw(G,with_labels=True)
plt.show()

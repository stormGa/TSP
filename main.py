# 旅行商问题
# 设有n个城市，城市之间的距离已知。
# 某旅行者希望从某个城市出发旅行完其余所有的城市最后回到出发的城市。
# 要求除起始出发的城市之外，其余的城市只能经过一次，求整个旅行的最短距离。
import networkx as nx
import numpy as np
from SA import  SA_FindPath
input_temp = input("输入城市数量，城市之间距离在10-100随机,n:")
n = int(input_temp)
G = nx.DiGraph()
seed = 0
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if i != j:
            random = np.random.RandomState(seed)  # 随机数种子，相同种子下每次运行生成的随机数相同
            seed += 1
            weight = random.randint(10, 100)
            #print(weight)
            G.add_weighted_edges_from([(j, i, weight), (i, j, weight)])  # 全连通图
            print('i:{0},j:{1},weight{2}'.format(i,j,weight))
#print(G.get_edge_data(1,2).get('weight'))
SA_FindPath(G,n,1)


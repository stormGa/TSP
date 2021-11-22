# 模拟退火算法
# @Author: LKH
# 参数
# @G ：图
# @start：起点
# @end： 结束
# @num_city: 城市数量
import math
import random

import networkx as nx


def cal_newpath(G, path, num_city):
    dis = 0
    DG = nx.DiGraph(G)
    i = 0
    while i < num_city:
        num1 = path[i]
        num2 = path[i + 1]
        dis = dis + DG.get_edge_data(num1, num2).get('weight')
        i = i + 1
    return dis


def SA_FindPath(G, num_city, start):
    initial_t = 100  # 初始温度
    lowest_t = 0.001  # 最低温度
    M = 5  # 当连续多次都不接受新的状态，开始改变温度
    iteration = 20  # 设置迭代次数
    path = list(range(1, num_city + 2))  # path = [1,2,3,....,num_city,1]
    path[num_city] = start

    # 初始化温度
    t_current = initial_t
    # 初始化距离
    dis = cal_newpath(G, path, num_city)
    while t_current > lowest_t:
        count_m = 0
        count_iter = 0
        while count_m < M and count_iter < iteration:
            # print('count_m<M,count:',count_iter)
            i = 0
            j = 0
            while i == j:
                i = random.randint(1, num_city - 1)
                j = random.randint(1, num_city - 1)
            path_new = path.copy()
            # 交换位置i，j,产生新解
            path_new[i], path_new[j] = path_new[j], path_new[i]
            dis_new = cal_newpath(G, path_new, num_city)
            # 求差
            dis_delta = dis_new - dis
            # 取0-1浮点随机数
            rand = random.random()
            # 计算指数函数的值
            exp_d = math.exp(-dis_delta / t_current)
            # 选择
            if dis_delta < 0:
                path = path_new
                dis = dis_new
            elif exp_d > rand:
                path = path_new
                dis = dis_new
            else:
                count_m = count_m + 1
            count_iter = count_iter + 1
            t_current = 0.99 * t_current  # 改变温度
            # print(path)
    dis_min = dis
    path_min = path
    print('最短距离：', dis_min)
    print('最短路径：', path_min)

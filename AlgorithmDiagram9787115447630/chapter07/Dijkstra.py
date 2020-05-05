""" 狄克斯特拉算法 """

""" 从起点到终点，找到耗时最短的路径：
 01 各个节点之间的关系图：
              
              6           1
         /--------> A --------\
        /           ^          \
       /            |           \_
 S(起点)             | 3         |----> F(终点)
       \            |           /
        \           |          /
         \--------> B --------/
              2           5
 
 """


# 搜索最短路径
def search(graph, costs, parents, processed):
    node = find_lowest_cost_node(costs, processed)  # 在未处理的节点中找出开销最小的节点
    while node is not None:  # 这个 while 循环在所有节点都被处理过后结束
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():  # 遍历当前节点的所有邻居
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:  # 如果经当前节点前往该邻居节点更近，
                costs[n] = new_cost  # 就更新该邻居的开销
                parents[n] = node  # 同时将该邻居的父节点设置为当前节点
        processed.append(node)  # 将当前节点标记为处理过
        node = find_lowest_cost_node(costs, processed)  # 找出接下来要处理的节点，并循环
    print("最短路径信息：")
    print(costs)
    print("父节点信息：")
    print(parents)


# 找出开销最小的节点
def find_lowest_cost_node(costs, processed):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:  # 遍历所有节点
        cost = costs[node]
        if cost < lowest_cost and node not in processed:  # 如果当前节点的开销更低且未处理过
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


# 初始化图的信息，使用三张散列表 graph, costs, parents 和一个数组 processed

# 节点关系表 graph
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

# 节点开销表
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# 节点的父节点关系表
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# 处理过的节点
processed = []

search(graph, costs, parents, processed)

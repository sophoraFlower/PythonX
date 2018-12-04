# coding:utf-8

graph = dict()
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
graph['fin'] = {}  # 终点没有邻居

infinity = float("inf")  # +oo正无穷
costs = dict()
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

parents = dict()
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

processed = []  # 已经处理过的点


def find_lowest_cost_node(cost):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:  # 遍历所有节点
        cost = costs[node]
        global processed
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def get_load(parents, destination):  # 获得路径
    t = parents.get(destination)
    print(destination, '<--', end=" ")
    while t:
        print(t, '<--', end=" ")
        t = parents.get(t)
    print('None')


node = find_lowest_cost_node(costs)
while node:  # 当还有节点可以处理的时候
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if new_cost < costs[n]:
            costs[n] = new_cost
            parents[n] = node

    processed.append(node)
    node = find_lowest_cost_node(costs)

print("cost is ", costs['fin'])

get_load(parents, 'fin')



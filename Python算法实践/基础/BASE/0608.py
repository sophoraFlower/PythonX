graph = dict()
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["a"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

print(graph)

infinity = float("inf")
costs = dict()
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

parents = dict()
parents["a"] = "start"
parents["b"] = "end"
parents["fin"] = None

processed = []


def find_lowest_cost_node(costs_):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node_ in costs_:
        cost_ = costs_[node_]
        if cost_ < lowest_cost and node_ not in processed:
            lowest_cost = cost_
            lowest_cost_node = node_
    return lowest_cost_node


node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
    print(costs)

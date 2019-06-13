"""
图是一组对象通过链接连接的一组对象的图形表示。
互连对象由称为顶点的点表示，连接顶点的链接称为边。
在这里详细描述了与图相关的各种术语和功能。
"""

'''
    a 。---------------。b
    |                  |
    |                  |
    |                  |
    |                  |
    |                  |
   c。-----------------。d--------------。e
   使用python字典数据类型轻松呈现图。 将顶点表示为字典的关键字，顶点之间的连接也称为边界，作为字典中的值。
'''
# Create the dictionary with graph elements
graph = {"a": ["b", "c"],
         "b": ["a", "d"],
         "c": ["a", "d"],
         "d": ["e"],
         "e": ["d"]
         }
print(graph)


# 显示圆的顶点
class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

    # Get the keys of the dictionary
    def get_vertices(self):
        return list(self.gdict.keys())

    def edges(self):
        return self.find_edges()

    # 添加一个顶点
    def add_vertex(self, vrtx):
        if vrtx not in self.gdict:
            self.gdict[vrtx] = []

    # 添加边
    def add_edge(self, edge):
        edge = set(edge)
        (vrtx1, vrtx2) = tuple(edge)
        if vrtx1 in self.gdict:
            self.gdict[vrtx1].append(vrtx2)
        else:
            self.gdict[vrtx1] = [vrtx2]

    def find_edges(self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
        return edgename


# Create the dictionary witgraph elements
graph_elements = {"a": ["b", "c"],
                  "b": ["a", "d"],
                  "c": ["a", "d"],
                  "d": ["e"],
                  "e": ["d"]
                  }

g = Graph(graph_elements)
print(g.get_vertices())
g.add_vertex("f")
print(g.get_vertices())
print(g.find_edges())
g.add_edge({'a', 'e'})
g.add_edge({'a', 'c'})
print(g.find_edges())

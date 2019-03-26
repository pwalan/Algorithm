class GraphNode:
    def __init__(self, value, entry=0, out=0, nexts=[], edges=[]):
        """
        :param value: int
        :param entry: int
        :param out: int
        :param nexts: Node[]
        :param edges: Edge[]
        """
        self.value = value
        # 入度
        self.entry = entry
        # 出度
        self.out = out
        # 后继节点
        self.nexts = nexts
        # 与本节点相连的边
        self.edges = edges


class Edge:
    def __init__(self, weight=0, from_where=None, to=None):
        """
        :param weight: float
        :param from_where: GraphNode
        :param to: GraphNode
        """
        self.weight = weight
        self.nexts = from_where
        self.edges = to


class Graph:
    def __init__(self, nodes={}, edges=set()):
        """
        :param nodes: {}
        :param edges: set()
        """
        self.nodes = nodes
        self.edges = edges


def create_graph(matrix):
    """
    :param matrix:[][]
    :return: Graph
    """
    graph = Graph()
    for i in range(len(matrix)):
        weight = matrix[i][0]
        from_where = matrix[i][1]
        to = matrix[i][2]

        if from_where not in graph.nodes.keys():
            graph.nodes[from_where] = GraphNode(from_where)
        if to not in graph.nodes.keys():
            graph.nodes[to] = GraphNode(to)

        from_node = graph.nodes[from_where]
        to_node = graph.nodes[to]
        new_edge = Edge(weight, from_node, to_node)

        from_node.nexts.append(to_node)
        from_node.out += 1
        to_node.entry += 1
        from_node.edges.append(new_edge)
        graph.edges.add(new_edge)

    return graph

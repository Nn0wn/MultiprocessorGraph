from typing import Union
from Graph.Node import Node
from Graph.Edge import Edge
from math import ceil


class Graph:

    def __init__(self, layers: int):
        self.__layers = [[] if i < layers else [Node(0, 0)] for i in range(layers + 1)]
        self.__edges = []

    def layers(self):
        return self.__layers

    def edges(self):
        return self.__edges

    def size(self):
        return sum([len(layer) for layer in self.__layers])

    def addNode(self, layer: int, weight: Union[int, float]):
        assert len(self.__layers) > layer > 0
        nodeId = self.size()
        self.__layers[layer - 1].append(Node(nodeId, weight))
        if layer == len(self.__layers) - 1:
            self.addEdge(nodeId, 0)

    def addEdge(self, idFrom: int, idTo: int):
        assert self.__checkChildEdges(idFrom, idTo) and self.__checkNodesLayer(idFrom, idTo)
        self.__edges.append(Edge(idFrom, idTo))

    def nodeLayer(self, id: int):
        for index, layer in enumerate(self.__layers, start=1):
            for node in layer:
                if node.id() == id:
                    return index

    def node(self, id: int):
        for layer in self.__layers:
            for node in layer:
                if node.id() == id:
                    return node

    def critical(self):
        return self.__layers[-1][0].critical()

    def criticalPath(self):
        return self.__layers[-1][0].criticalPath()

    def process(self):
        for layer in self.__layers:
            for node in layer:
                prevNodes = []
                for edge in self.__edges:
                    if edge.idTo() == node.id():
                        prevNodes.append(self.node(edge.idFrom()))
                else:
                    if len(prevNodes) > 0:
                        prevNode = max(prevNodes, key=lambda _node: _node.critical())
                        node.setCritical(prevNode.critical() + node.weight())
                        node.setCriticalPath(prevNode.criticalPath().copy())
                        node.criticalPath().append(prevNode.id())
                    else:
                        node.setCritical(node.critical() + node.weight())

    def getProcessors(self):
        allWeights = sum([node.weight() for layer in self.__layers for node in layer])
        critical = self.__layers[-1][0].critical()
        return [0 if critical == 0 else ceil(allWeights / critical)][0]

    def __checkNodesLayer(self, idFrom: int, idTo: int):
        fromNodeLayer = self.nodeLayer(idFrom)
        toNodeLayer = self.nodeLayer(idTo)
        if fromNodeLayer and toNodeLayer and fromNodeLayer <= toNodeLayer:
            return True
        return False

    def __checkChildEdges(self, idFrom: int, idTo: int):
        for edge in self.__edges:
            if edge.idFrom() == idFrom and edge.idTo() == idTo:
                return False
            elif edge.idTo() == idTo:
                if not self.__checkChildEdges(idFrom, edge.idFrom()):
                    return False
        return True

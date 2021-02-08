from random import randint, seed
from Graph.Graph import Graph
from Table.ProcessorTable import ProcessorTable

seed(8)

weights = [[randint(1, 10) * 10 for _ in range(2)],
           [randint(1, 10) * 10 for _ in range(3)],
           [randint(1, 10) * 10 for _ in range(3)],
           [randint(1, 10) * 10 for _ in range(2)],
           [randint(1, 10) * 10 for _ in range(3)]]
# weights = [[10, 60], [70, 40, 90], [30, 30, 60], [20, 10], [80, 70, 50]]

print('-' * 25 + ' Nodes processing times ' + '-' * 25)
for lindex, layer in enumerate(weights):
    nodes = ''
    for nindex, node in enumerate(layer):
        nodes = nodes + str(' [Id: {}, Time: {}] '.format(nindex + 1, node))
    print('Layer:', lindex + 1, '\tNodes:', nodes)

edges = [[1, 4], [2, 4], [3, 6], [4, 6], [4, 7], [4, 8], [5, 8], [6, 9],
         [6, 10], [7, 10], [8, 10], [9, 11], [10, 11], [10, 12], [10, 13]]

graph = Graph(5)
for index, layer in enumerate(weights, start=1):
    for weight in layer:
        graph.addNode(index, weight)
for edge in edges:
    graph.addEdge(edge[0], edge[1])
graph.process()

print('-' * 25 + ' Graph critical weight: ' + str(graph.critical()) + ' ' + '-' * 25)
print('-' * 25 + ' Graph critical path: ' + ''.join(str(i) + ' -> ' for i in graph.criticalPath()[:-1]) +
      str(graph.criticalPath()[-1]) + ' ' + '-' * 25)
print('-' * 25 + ' Graph optimal processor count: ' + str(graph.getProcessors()) + ' ' + '-' * 25)
print()
# print('*' * 25 + ' Processor loading table ' + '*' * 25)

table = ProcessorTable(graph)
table.process()
table.print()


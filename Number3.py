import Graph
import Operations

n = 5
graphA = []
graphB = []

Graph.generator_matrix(graphA, 4)
Graph.print_matrix(graphA, 0, 4)
print()

Graph.generator_matrix(graphB, 5)
Graph.print_matrix(graphB, 0, 5)
print()

graphC = []
for i in range(n):
    a = []
    for j in range(n):
        a.append(0)
    graphC.append(a)

Operations.crossroads_graphs(graphA, graphB, graphC, 4)
Graph.print_matrix(graphC, 0, 5)


graphD = []
for i in range(n):
    a = []
    for j in range(n):
        a.append(0)
    graphD.append(a)

Operations.circle_sum_graphs(graphA, graphB, graphD, n)
Graph.print_matrix(graphD, 0, len(graphD))


graph1 = []
graph2 = []

Graph.generator_matrix(graph1, 4)
Graph.print_matrix(graph1, 0, 4)

Graph.generator_matrix(graph2, 3)
Graph.print_matrix(graph2, 2, 5)

Operations.unification_graphs(graph1, graph2, 2)
Graph.print_matrix(graph1, 0, 5)

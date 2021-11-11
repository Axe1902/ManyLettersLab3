import Graph
import Operations

n = int(input("Введите размер матрицы: "))

#graph = []
graph = [[0, 1, 1, 0, 0, 1],
         [1, 0, 0, 1, 0, 0],
         [1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0],
         [1, 0, 0, 0, 0, 0]]
line = []
#Graph.generator_matrix(graph, n)
Graph.print_matrix(graph, 0, n)
Graph.generator_line(line, graph, n)

Dist = [-1 for _ in range(n)]

node = int(input("Введите номер вершины: "))
Operations.bfsd_matrix(graph, Dist, node-1)
print(Dist)
print()

Dist = [-1 for _ in range(n)]
Operations.bfsd_line(line, Dist, node-1)
print(Dist)
print()

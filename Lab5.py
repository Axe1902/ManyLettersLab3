import Graph
import Operations

n = int(input("Введите размер матрицы: "))

graph = []
# graph = [[0, 1, 1, 0, 0, 1],
#          [1, 0, 0, 1, 0, 0],
#          [1, 0, 0, 0, 1, 0],
#          [0, 1, 0, 0, 0, 0],
#          [0, 0, 1, 0, 0, 0],
#          [1, 0, 0, 0, 0, 0]]
line = []
Graph.generator_matrix(graph, n)
Graph.print_matrix(graph, 0, n)
Graph.generator_line(line, graph, n)

Visits = [0 for _ in range(n)]

node = int(input("Введите номер вершины: "))
Operations.bfs_matrix(graph, Visits, node-1)
print()

Visits = [0 for _ in range(n)]
Operations.bfs_line(line, Visits, node-1)
print()

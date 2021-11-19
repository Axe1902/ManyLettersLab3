import Graph
import Operations

n = int(input("Введите размер матрицы: "))

graph = []
# graph = [[0, 2, 3, 0, 0, 1],
#          [2, 0, 0, 5, 0, 0],
#          [3, 0, 0, 0, 1, 0],
#          [0, 5, 0, 0, 0, 0],
#          [0, 0, 1, 0, 0, 0],
#          [1, 0, 0, 0, 0, 0]]
line = []
Graph.generator_w_matrix(graph, n, 8)
Graph.print_matrix(graph, 0, n)
Graph.generator_line(line, graph, n)

Dist = [1000 for _ in range(n)]

node = int(input("Введите номер вершины: "))
Operations.bfsd_matrix_real(graph, Dist, node-1)
print()

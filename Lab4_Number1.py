import Graph
import Operations

n = int(input("Введите размер матрицы: "))

graph = []
line = []
Graph.generator_matrix(graph, n)
Graph.print_matrix(graph, 0, n)
Graph.generator_line(line, graph, n)

Visits = [0 for _ in range(n)]

node = int(input("Введите номер вершины: "))
Operations.depth_first_search_matrix(graph, Visits, node-1)
print()

Visits = [0 for _ in range(n)]
Operations.depth_first_search_line(line, Visits, node-1)
print()

Visits = [0 for _ in range(n)]
Operations.depth_first_search_stack(graph, Visits, node-1)

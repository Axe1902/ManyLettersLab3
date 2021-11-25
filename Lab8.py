import Graph
import Operations

n = int(input("Введите размер матрицы: "))

graph = []
Graph.generator_w_matrix(graph, n, 3)
# graph = [[0, 2, 3, 0, 0, 1],
#          [2, 0, 0, 5, 0, 0],
#          [3, 0, 0, 0, 1, 0],
#          [0, 5, 0, 0, 0, 0],
#          [0, 0, 1, 0, 0, 0],
#          [1, 0, 0, 0, 0, 0]]
Graph.print_matrix(graph, 0, n)

eccentricity = []
for i in range(n):
    Dist = [1000 for _ in range(n)]
    Operations.bfsd_matrix_real(graph, Dist, i)
    print()
    eccentricity.append(max(Dist))

print("Эксцентриситет: ", eccentricity)
Diameter = max(eccentricity)
Radius = min(eccentricity)
print("Диамерт: ", Diameter)
print("Радиус: ", Radius)

peripheralNode = []
centralNode = []
Operations.search_peripheral_or_central_node(eccentricity, Diameter, peripheralNode)
Operations.search_peripheral_or_central_node(eccentricity, Radius, centralNode)
print("Переферийные вершины: ", peripheralNode)
print("Центральные вершины: ", centralNode)

Degrees = [0 for _ in range(n)]
isolationNode = []
endNode = []
dominationNode = []

Operations.degree_of_node(graph, Degrees, n)
for i in range(n):
    if Degrees[i] == 0:
        isolationNode.append(i + 1)
    elif Degrees[i] == 1:
        endNode.append(i + 1)
    elif Degrees[i] == n - 1:
        dominationNode.append(i + 1)

print("Изолированные вершины:", isolationNode)
print("Концевые вершины:", endNode)
print("Доминирующие вершины:", dominationNode)
print()

incGraph = []
edge = []
Visits = [0 for _ in range(n)]
Graph.generator_incident_matrix(graph, edge, incGraph, Visits, n)

eccentricityInc = []
for i in range(n):
    Dist = [1000 for _ in range(n)]
    Operations.bfsd_incMatrix_real(incGraph, edge, Dist, i)
    print()
    eccentricityInc.append(max(Dist))

print("Эксцентриситет: ", eccentricityInc)
Diameter = max(eccentricityInc)
Radius = min(eccentricityInc)
print("Диамерт: ", Diameter)
print("Радиус: ", Radius)

peripheralNodeInc = []
centralNodeInc = []
Operations.search_peripheral_or_central_node(eccentricity, Diameter, peripheralNodeInc)
Operations.search_peripheral_or_central_node(eccentricity, Radius, centralNodeInc)
print("Переферийные вершины: ", peripheralNodeInc)
print("Центральные вершины: ", centralNodeInc)
